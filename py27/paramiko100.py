#!/usr/bin/env python

import paramiko
import time
import os


def get_command_output(cmd, remote_conn, inFile, vsh, vsh_lc):
    '''Execute command & captures output in inFile'''

    remote_conn.send(cmd)

    # Wait for the command to start generating output
    time.sleep(3)

    not_done = True
    MAX_RETRY = 5

    while (not_done or MAX_RETRY > 0):
        if remote_conn.recv_ready():
            output = remote_conn.recv(65535)
            inFile.write(output)
            output = 0
            if MAX_RETRY < 5:
                print ("RESET RETRY")
                MAX_RETRY = 5
        else:
            not_done = False
            MAX_RETRY = MAX_RETRY - 1


if __name__ == '__main__':


    # VARIABLES THAT NEED CHANGED
    ip = '172.68.100'
    username = 'admin'
    password = 'pass'

    # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(
         paramiko.AutoAddPolicy())

    # initiate SSH connection
    remote_conn_pre.connect(ip, username=username, password=password, 
                            look_for_keys=False, allow_agent=False)
    print "SSH connection established to %s" % ip

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print "Interactive SSH session established"

    disable_paging(remote_conn)

    # Login to IFC, get show switch o/p
    remote_conn.send("\n")
    remote_conn.send("show switch > show_switch_op\n")
    time.sleep(2)
    os.system("sshpass -p 'pass' scp -o StrictHostKeyChecking=no 
               admin@172.68.1.100:/home/admin/show_switch_op ./")
    os.system("cat show_switch_op | tr -s ' ' > show_switch_op.tmp")

    # File manipulation to get addresses
    ingredients = file("show_switch_op.tmp", 'r')
    cols, indexToName =  getColumns(ingredients)
    ingredients.close()
    num_of_nodes = len(cols[3])
    for switch_cnt in range(2, num_of_nodes-1):
        inband_addr = cols[3][switch_cnt]
        print (inband_addr)

        cmd1 = "sshpass -p 'pass' ssh " + str(inband_addr)
        #print (cmd1)
        remote_conn.send(cmd1 + "\n")
        time.sleep(10)

        switch_name = str(cols[11][switch_cnt])
        filename = "tech_support_" + str(cols[11][switch_cnt])
        filepath = "/var/log/"
        file = filepath + filename
        print (file)
        f = open(str(filename), 'a+')

        # Clear the buffer
        output = remote_conn.recv(1000)
        output = 0

        remote_conn.send("\n")
        print ("DEBUG LOG END READ WRITE START " + switch_name + " 
               !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        get_command_output("show ip route vrf all\n", remote_conn, f, 
                           False, False)
        f.close()
        print ("DEBUG LOG END READ WRITE COMPLETE " + switch_name + " 
                !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        remote_conn.send("\n")
        time.sleep(1)

        # Exit from switch & back to IFC
        remote_conn.send("exit\n")
        time.sleep(1)

        # Close the connection and open a new one
        # XXX If same ssh connection is used for multiple send/rcv then it 
        # crashes.
        # Hence opening new connection for every switch.
        remote_conn.close();

        # Create instance of SSHClient object
        remote_conn_pre = paramiko.SSHClient()

        # Automatically add untrusted hosts (make sure okay for security policy 
        #   in your environment)
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # initiate SSH connection
        remote_conn_pre.connect(ip, username=username, password=password,    
                                 look_for_keys=False, allow_agent=False)
        print "SSH connection established to %s" % ip

        # Use invoke_shell to establish an 'interactive session'
        remote_conn = remote_conn_pre.invoke_shell()
        print "Interactive SSH session established"

        disable_paging(remote_conn)

    remote_conn.close()
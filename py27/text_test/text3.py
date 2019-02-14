import binascii

text = "Simply Easy Learning"

# Converting binary to ascii
data_b2a = binascii.b2a_uu(text)
print "**Binary to Ascii** \n"
print data_b2a

# Converting back from ascii to binary 
data_a2b = binascii.a2b_uu(data_b2a)
print "**Ascii to Binary** \n"
print data_a2b
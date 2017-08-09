import os

'''
Script to populate VLA with:

Vocab, EE Science I, EE Science II, and Users
'''



# Start execution here!
if __name__ == '__main__':
    print "Starting VLA population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VLA_project.settings')
    execfile("populate_vocab.py")
    execfile("populate_EE1.py")
    #execfile("populate_EE2.py")

    print "Populating EE2"
    execfile("./populate/populate_ECE2323_1.py")
    execfile("populate_users.py")
    execfile("./populate/populate_ECE2323_2.py")
    execfile("./populate/populate_ECE2323_3.py")
    execfile("./populate/populate_ECE2323_4.py")
    execfile("./populate/populate_ECE2323_5.py")
    execfile("./populate/populate_ECE2323_6.py")
    execfile("./populate/populate_ECE2323_7.py")
    execfile("./populate/populate_ECE2323_8.py")
    execfile("./populate/populate_ECE2323_9.py")
    execfile("./populate/populate_ECE2323_10.py")
    execfile("./populate/populate_ECE2323_11.py")

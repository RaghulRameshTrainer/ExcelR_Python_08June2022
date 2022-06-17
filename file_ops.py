'''
with open(filename, mode) as fh:
    pass
mode
r (read)-> Open the file to read, File must exists. If the file is not there then
            we will get FileNotFoundError
            read(), readline(), readlines()
w (write) -> Open the file for writing . If the file is not there it will create a
            file and write into it. OR if the file is there, then it will cleanup
            the file content and start writing as a new file
            write(), writelines()
a (append)  -> similar to write except it will not remove the file content, it will
                continue to add the content along with the existing data
r+( read and write) -> file we must read the existing content and start writing into it
w+ ( write and read) -> write first and read whatever has been written
rb (read binary) -> image,video,audio
wb (write binary)
'''

#with open('day.txt','r') as fo:
    #print(fo.read())
     # print(fo.readline(),end='')
     # print(fo.readline())
    #print(fo.readlines()[1:6])
    # for day in fo.readlines()[1:6]:
    #     print(day.upper(),end='')

# with open(r'D:\data\tech.txt') as fh:
#     print(fh.read())

# with open(r'D:\data\tech.txt','w') as fh:
#     fh.writelines(["Data Analytics\n","PowerBI"])

# with open(r'D:\data\tech.txt', 'a') as fh:
#     fh.writelines(["\nMySQL\n", "R"])

# with open('day.txt','r+') as fh:
#     print(fh.read())
#     fh.writelines(['\nINDIA\n','PAKISTAN'])
#     # fh.writelines(['Artificial Intellegence , Machine Learning\n','Deep Learning'])
#     # print(fh.read())

# with open('day.txt','w+') as fo:
#     fo.writelines(['Chennai\n','Bangalore\n','Hyderabad\n','Pune\n','Delhi'])
#     fo.seek(0,0)
#     print(fo.read())

# with open('day.txt') as rf:
#     with open('city.txt','a') as wf:
#         data=rf.readlines()
#         wf.writelines(data[0:2])
#         wf.writelines(['Cochin\n','Kolkatta\n'])
#         wf.writelines(data[2:])

with open(r'C:\Users\RaghulRamesh\OneDrive\Pictures\puppy.jpg','rb') as pp:
    with open(r'C:\Users\RaghulRamesh\OneDrive\Pictures\puppy_new.jpg', 'wb') as wp:
        wp.write(pp.read())
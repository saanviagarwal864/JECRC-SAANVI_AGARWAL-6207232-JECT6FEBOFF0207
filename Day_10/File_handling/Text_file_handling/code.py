'''
File Handling
--> File is a type of container in which we contain or store some data.
--> by using extension name we can identify what type of data is there insisde of it.
ex: .py,.mp4,.html,.mp3,.png,.jpg,.jpeg etc.
--> Before handling any file, taking permission is very much important.

open():
   open('filename.ext'/'absolute_path',mode)

close():
   var_name.close()

--> here total 3 different modes are present,
   1. write(w)
   2. read(r)
   3. append(a)

--> write mode:
1. only write(w),
2. write+read(w+)
3. write binary (wb)
4. write and read binary (wb+)

--> read mode:
1. only read(r),
2. read+write(r+) ##first read then write
3. read binary (rb)
4. read and write binary (rb+)

--> append mode:
1. only append(a),
2. append+read(a+)
3. append binary (ab)
4. append and read binary (ab+)


##For write operation,
1. write(str_data): single line of data
2. writelines([line1, line2, ..., linen]): multiple line of data

NOTE:
1. IN this if the file is ot present it will create one then perform write operation
2. If the file is already present, then it will override the prev data with the new one.

##For read operation,
1. read()-> display the file content as it is.
2. readline()-> display single line of data at a time
3. readlines()-> the way i have written the dat in the same way it will return the output

##For write and append operation,
1. write()->single line
2. writelines()->multiple lines


'''

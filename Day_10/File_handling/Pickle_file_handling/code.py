'''
Pickle same as json but converts files in binary instead of string so we use ab+ to read binary file
'''
import pickle

file=open('pickle.txt','ab+')
data={
    'fullname': 'saanvi agarwal',
    'userid' : 65674573478,
    'password' : '*****'
}
# print(f'Original Data: {data}')
# print(f'Type of original Data: {type(data)}') ##dict
# print()

# enc_data=pickle.dumps(data)
# print(f'Encrypted Data: {enc_data}')
# print(f'Type of encrypted Data: {type(enc_data)}') ##string

# dec_data=pickle.loads(enc_data)
# print(f'Decrypted Data: {dec_data}')
# print(f'Type of decrypted Data: {type(dec_data)}') ###dict

enc_data=pickle.dumps(data)
file.write(enc_data)

file.seek(0)

enc_data=file.read()
print(type(enc_data)) ##it will be string

ori_data=pickle.loads(enc_data)
print(ori_data,type(ori_data)) ##original data will be in dict


file.close()

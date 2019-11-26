import json

with open("data.json", encoding='utf-8') as f:
	data = json.load(f)

#Chuẩn hóa về 0-1
phone1 = []


# for key in data:
# 	name.append(key)
# 	phone.append(int(data[key]))

#Sort
def insertionSort(b): 
    for i in range(1, len(b)): 
        up = b[i] 
        j = i - 1
        while j >=0 and b[j] > up:  
            b[j + 1] = b[j] 
            j -= 1
        b[j + 1] = up      
    return b      
              
def bucketSort(x): 
    arr = [] 
    slot_num = 10 

    for i in range(slot_num): 
        arr.append([]) 
          
    # 10 buckets 
    for j in x: 
        index_b = int(slot_num * j)  
        arr[index_b].append(j) 
      
    # Sort buckets  
    for i in range(slot_num): 
        arr[i] = insertionSort(arr[i]) 
          
    # concatenate bucket 
    k = 0
    for i in range(slot_num): 
        for j in range(len(arr[i])): 
            x[k] = arr[i][j] 
            k += 1
    return x 

#Menu

def showContacts():
	with open("data.json", encoding='utf-8') as f:
		data = json.load(f)
	print("Dạnh bạ : ")
	for x in data :
		print(x + ":" + data[x])

def addContacts():
	print("Nhập tên : ")
	name = input()
	print("Nhập số điện thoại : ")
	phoneNumber = input()
	data[name] = phoneNumber

	with open("data.json", 'w', encoding='utf-8') as f:
		json.dump(data, f)

def editContacts():
	print("Nhập tên muốn sửa : ")
	name = input()

	if name in data:
		print("Nhập tên mới : ")
		newName = input()
		print("Nhập số điện thoại mới : ")
		newPhoneNumber = input()
		data.pop(name)
		data[newName] = newPhoneNumber
		with open("data.json", 'w', encoding='utf-8') as f:
			json.dump(data, f)
	else:
		print("Không tìm thấy người này !")

def deleteContacts():
	print("Nhập tên muốn xóa : ")
	name = input()
	if name in data:
		data.pop(name)
		with open("data.json", 'w', encoding='utf-8') as f:
			json.dump(data, f)
	else:
		print("Không tìm thấy người này !")

def sortContacts():
	for i,j in data.items():
		phone1.append(int(j)/1000000000)
	# for i in phone:
		# print(i)
	bucketSort(phone1)

	dataSorted = {}

	for x in phone1:
		for name, phonex in data.items():
			if int(phonex) == x*1000000000:
				dataSorted[name] = phonex
	with open("data.json", 'w', encoding='utf-8') as f:
		json.dump(dataSorted, f)
	print("Đã sắp xếp theo số điện thoại !")

def searchContact():
	pass

def menu():
	print("1. Hiển thị số điện thoại")
	print("2. Thêm số điện thoại")
	print("3. Sửa số điện thoại")
	print("4. Xóa số điện thoại")
	print("5. Sắp xếp số điện thoại")
	print("6. Thoát")
	s = input()

	if(s == '1'):
		showContacts()
		menu()
	elif(s == '2'):
		addContacts()
		menu()
	elif(s == '3'):
		editContacts()
		menu()
	elif(s == '4'):
		deleteContacts()
		menu()
	elif(s == '5'):
		sortContacts()
		menu()
	else:
		exit()


if __name__ == '__main__':
	menu()

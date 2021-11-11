# PassMan – Password Manager

**Prepared by:-**

#### 1) Anish Agarwal

#### 2) Raktim Saha

#### Indian Institute of Information Technology (IIIT), Kalyani

#### October 24, 2021

## Introduction

#### Project Scope

The software can generate and keep track of several user credentials for different websites
and/ or services. It will be designed to maximize user safety and convenience in their
online activities, by generating strong passwords as well as keeping track of them, so that
the user need not remember complex credentials for different online services.

The user is initially required to register with an email address and verify with the OTP,
thereby setting a master password to the product. Thereafter, the user only needs to
remember and input the master password to the software in order to retrieve the saved
passwords for various websites.

The software makes use of a database to store the usernames and passwords in
encrypted forms, which is retrieved every time the user requests them.

#### References

The software uses the following software specifications and dependencies to work properly:

- Python v3.9+ https://www.python.org/
- Tkinter (GUI) https://docs.python.org/3/library/tkinter.html
- Sqlite (Database access) https://docs.python.org/3/library/sqlite3.html
- smtplib (Sending Email) https://docs.python.org/3/library/smtplib.html
- Cryptography (Encryption) https://cryptography.io/en/latest/
- Subprocess (Clipboard access) https://docs.python.org/3/library/subprocess.html
- Hashlib (hashing Master Password) https://cryptography.io/en/latest/

Fernet encryption key references (Cryptography) https://cryptography.io/en/latest/fernet/

## Overall Description

#### Product Perspective

_This product is standalone in the field of password manager services and it doesn’t require an_
internet connection, unlike many similar products. It works offline and stores the credentials in a
local database on the user system.

#### Product Features

On initial use, the user is required to register an email address which will be used thereafter to
authenticate the user and send password reset OTPs in case the user forgets the password.
The software creates a **_“pwmdatabase.db”_** file and a **_“secret.key”_** file in the current directory of
the binary (or where the PassMan.py file is located in the script is executed).
NOTE:- Both these files contain sensitive information and MUST NOT BE shared.

Once the user has registered with an email address, the login process only requires the master
password, which the user had to enter during registration. This password is then checked against
the registered email ID and the user is allowed/ denied entry based on its correctness.

In case the user is unable to provide the correct master password, s/he can opt for a password
change by sending and verifying an OTP sent to the registered email address, post which, the user
can change their password.

Once the user gains entry post logging in successfully, s/he is presented with a screen listing all
the websites/ services for which credentials are saved in the database. The user can choose to
add new sets of credentials for a service or fetch credentials for a saved website/ service.

After fetching the credentials (username and password) for a particular service, the user can
choose to either copy the password into their clipboard or even delete the saved credentials.
After adding a credential, the list can be updated by clicking on the small green button on the top
right-hand side (REFRESH).
The user can log out of the software by clicking the small red button on the top right-hand side
(LOGOUT)

#### User Classes and Characteristics

Users of the product should be able to:-

- Add and save credentials for a specific website/ service
  o Save their own username and password pair.
  o Generate a password by the software and save it.
- View a list of all services for which credentials are saved.
- Retrieve the credentials for a given website/ service searching by its name.
- Copying the password for service after retrieving from the database.
- Deleting the saved credentials for the retrieved service.

#### Add Credentials

**Description and Priority**
Post successful login, the user is presented with a screen listing all the sites/
services for which the database has saved the credentials. Initially, this list will be
empty, and the User will be able to add credentials for a particular website/ service

The add credentials section will ask the User for the name of the service, their
username and password. The User also has the option to generate a new password
and save it for the specified service, which will then be generated by the software
and saved into the database.

The software makes use of the Fernet key from the Cryptography module of Python
3.9, which is used to create a URL safe, base64 encoded encryption token, which
encrypts the original password and guarantees strong privacy and authenticity.
The key used is a 128-bit key that uses AES in CBC mode and initialization vectors
generated from os.urandom() method.

#### Search Credentials

**Description**
The user should be able to search for the saved credentials to a given website/
service, providing the name (in full or partial) of the service.
The software queries the database for the name as entered by the User, and returns
the following: -
i) Site Name
ii) Username
iii) Password
The user should also have options to either copy the password into their clipboard
or delete the selected (fetched) credential set from the database.

#### Delete Credentials

**Description**
The User has the ability to delete selected credentials from the database. The user
first needs to fetch the credentials using the Search method, and once the
credentials along with the site name have been fetched, the User can delete the
selected record by clicking on the delete button.
Home | Add/Del  | Get
:---: | :---: | :---:
![pic1](https://user-images.githubusercontent.com/43948081/141369121-2c55fa58-fb38-4946-a233-7d2054bb557a.png)|![pic2](https://user-images.githubusercontent.com/43948081/141369125-86b7e8f3-8bdf-44b9-8967-8c0e47890f33.png)|![pic3](https://user-images.githubusercontent.com/43948081/141369128-4387b1de-3d27-4901-8368-68047b3887f2.png)

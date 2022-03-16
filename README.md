# Android-PIN-BruteForce
Python script to brute force Android Pin Lock

# Step 1
Create adb access to a rooted android device. Santoku can be used to get this done

# Step 2
Pull settings.db from phone using 'adb pull /data/data/com.android.providers.setings/databases/settings.db' . The db is a sqllite db and it contains a tabled named "secure". Secure has a locksettings filed that contains the password salt. 

# Step 3
Pull password hash using 'adb pull /data/system/password.key'. This contains MD5 & SHA1 hashes.

# usage:
    - python3 androidpincrack.py <salt> <pin length>
  - example
    - `` python3 androidpincrack.py 34526724572864372452478 4 ``

''Note password.key should be in the same file''

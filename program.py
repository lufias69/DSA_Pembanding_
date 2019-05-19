import utils as ut
from textwrap import wrap
msg = 'Please write your message'
p = ut.get_rdm_prime_nb()
q = ut.get_rdm_prime_nb(to_ignore=[p])
print(f'p = {p} ; q = {q}')

pub_k, priv_k = ut.gen_keys(p, q)

print(f'public key: {pub_k}\nprivate key: {priv_k}')
#print()
ciphertext = ut.encrypt(pub_k, msg)
txt = ''.join(map(lambda x: str(x), ciphertext))
print("decrypted message:")
print('\n'.join(wrap(txt, width=70)))

#yang dikrim
#1. ciphertext (sudah dienkripsi)
#2. priv_k
#3. msg (pesan aslinya)

#tes haspus yang gagal
#ciphertext[1]=7334118089

print()
print("verifikasi :")
try:
    decrypted = ut.decrypt(priv_k, ciphertext)
    #print("    "+''.join(map(lambda x: str(x), decrypted)))
    if ''.join(map(lambda x: str(x), decrypted)) == msg:
        print('    message:')
        print("      "+''.join(map(lambda x: str(x), decrypted)))
        print("      ---------Succes---------")
    else:
        print("    ---------Failed---------")
except:
    print("    ---------Failed---------")
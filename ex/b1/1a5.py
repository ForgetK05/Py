a, b = map(float, input().split())

x, y = map(int, input().split())

p = int(input())

dien_tich_phong = a * b

dien_tich_gach = (x * y) / 10000  

so_gach = int((dien_tich_phong / dien_tich_gach) * 1.1)

chi_phi_gach = so_gach * p
chi_phi_nhan_cong = int(dien_tich_phong * 100000)
tong_chi_phi = chi_phi_gach + chi_phi_nhan_cong

print(f"{dien_tich_phong:.2f}") 
print(so_gach) 
print(chi_phi_gach) 
print(chi_phi_nhan_cong)
print(tong_chi_phi)
ds_hoc_sinh = [
    ["Lương Diệu An",8,9,8],
    ["Đặng Bình Ân",7,8,8],
    ["Trần Thị Minh Anh",9,8,7],
    ["Lê Hoàng Bảo",10,9,8],
    ["Phạm Quốc Dũng",7,8,8],
    ["Hoàng Thị Thu Hà",9,9,10],
    ["Võ Minh Hùng",8,6,7],
    ["Đặng Ngọc Lan",10,8,9],
    ["Bùi Thành Minh",7,7,8],
    ["Phan Thị Ngọc",9,8,9],
    ["Đỗ Anh Tuấn",8,9,7]
    ]
print ("{:<25} {:<18} {:<15} {:<15}".format("Họ và tên", "Điểm chuyên cần", "Điểm giữa kỳ", "Điểm cuối kỳ"))
for hs in ds_hoc_sinh:
    print("{:<25} {:<18} {:<15} {:<15}".format(hs[0], hs[1], hs[2], hs[3]))
for hs in ds_hoc_sinh:
    Tong_ket = hs[1]*0.2 + hs[2]*0.3 + hs[3]*0.5
    hs.append(round(Tong_ket,2))
print ("{:<25} {:<18} {:<15} {:<15} {:<12}".format("Họ và tên", "Điểm chuyên cần", "Điểm giữa kỳ", "Điểm cuối kỳ", "Tổng kết"))
for hs in ds_hoc_sinh:
    print("{:<25} {:<18} {:<15} {:<15} {:<12}".format(hs[0], hs[1], hs[2], hs[3], hs[4]))
for hs in ds_hoc_sinh:
    if hs[4] >= 8.5:
        xep_loai = "Giỏi"
    elif 7.0 <= hs[4] <8.5:
        xep_loai = "Khá"
    elif 5.0 <= hs[4] < 7.0:
        xep_loai = "Trung bình"
    elif hs[4] < 5:   
        xep_loai = "Yếu"
    hs.append(xep_loai)
print ("{:<25} {:<18} {:<15} {:<15} {:<12} {:<15}".format("Họ và tên", "Điểm chuyên cần", "Điểm giữa kỳ", "Điểm cuối kỳ", "Tổng kết", "Xếp loại"))
for hs in ds_hoc_sinh:
    print("{:<25} {:<18} {:<15} {:<15} {:<12}{:<15} ".format(hs[0], hs[1], hs[2], hs[3], hs[4], hs[5]))
tong_diem = 0
for hs in ds_hoc_sinh:
    tong_diem = tong_diem + hs[4]
diem_trung_binh = tong_diem / len(ds_hoc_sinh)
print("Điểm tổng kết trung bình của lớp:", round(diem_trung_binh, 2))
hs_cao_nhat = ds_hoc_sinh[0]
for hs in ds_hoc_sinh:
    if hs[4] > hs_cao_nhat[4]:
        hs_cao_nhat = hs
print("Học sinh có điểm cao nhất:", hs_cao_nhat[0])
print("Điểm tổng kết:", hs_cao_nhat[4])
hs_thap_nhat = ds_hoc_sinh[0]
for hs in ds_hoc_sinh:
    if hs[4] < hs_thap_nhat[4]:
        hs_thap_nhat = hs
print("Học sinh có điểm thấp nhất:", hs_thap_nhat[0])
print("Điểm tổng kết:", hs_thap_nhat[4])
so_hoc_sinh_dat = 0
for hs in ds_hoc_sinh:
    if hs[4] >=5:
        so_hoc_sinh_dat = so_hoc_sinh_dat + 1
print("Số học sinh đạt:", so_hoc_sinh_dat)
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
ten = []
diem = []
for hs in ds_hoc_sinh:
    ten.append(hs[0])
    diem.append(hs[4])
plt.barh(ten, diem)
plt.title("Điểm tổng kết của 10 học sinh")
plt.xlabel("Điểm tổng kết")
plt.ylabel("Họ và tên")
plt.xlim(0,10)
plt.show()
            

    
      


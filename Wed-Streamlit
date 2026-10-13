import streamlit as st
import matplotlib.pyplot as plt
#Danh sách dữ liệu học sinh
ds_sinh_vien = [
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
    ]

#Tính điểm tổng kết
for hs in ds_sinh_vien:
    Tong_ket = hs[1]*0.2 + hs[2]*0.3 + hs[3]*0.5
    hs.append(round(Tong_ket,2))
#Xếp loại học sinh
for hs in ds_sinh_vien:
    if hs[4] >= 8.5:
        xep_loai = "Giỏi"
    elif 7.0 <= hs[4] <8.5:
        xep_loai = "Khá"
    elif 5.0 <= hs[4] < 7.0:
        xep_loai = "Trung bình"
    elif hs[4] < 5:   
        xep_loai = "Yếu"
    hs.append(xep_loai)
# Tieu de trang web
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
# Hien thi bang diem
st.subheader("Bảng điểm 10 sinh viên")
bang_diem = []

for hs in ds_sinh_vien:
    bang_diem.append({
        "Họ tên": hs[0],
        "Chuyên cần": hs[1],
        "Giữa kỳ": hs[2],
        "Cuối kỳ": hs[3],
        "Tổng kết": hs[4],
        "Xếp loại": hs[5]
    })
st.table(bang_diem)
#Điểm tổng kết trung bình cả lớp
tong_diem = 0
for hs in ds_sinh_vien:
    tong_diem = tong_diem + hs[4]
diem_trung_binh = tong_diem / len(ds_sinh_vien)
st.subheader("Thống kê kết quả")
st.write("Điểm trung bình của lớp:", round(diem_trung_binh, 2))
#Học sinh có điểm tổng kết cao nhất
sv_cao_nhat = ds_sinh_vien[0]
for hs in ds_sinh_vien:
    if hs[4] > sv_cao_nhat[4]:
        sv_cao_nhat = hs
sv_thap_nhat = ds_sinh_vien[0]
for hs in ds_sinh_vien:
    if hs[4] < sv_thap_nhat[4]:
        sv_thap_nhat = hs
st.write("Sinh viên cao điểm nhất:", sv_cao_nhat[0],
         "-", sv_cao_nhat[4])
st.write("Sinh viên thấp điểm nhất:", sv_thap_nhat[0],
         "-", sv_thap_nhat[4])
so_sinh_vien_dat = 0
for hs in ds_sinh_vien:
    if hs[4] >=5:
        so_sinh_vien_dat = so_sinh_vien_dat + 1
st.write("Số sinh viên đạt:", so_sinh_vien_dat)
# Danh sach xổ xuống chọn sinh viên
st.subheader("Tra cứu điểm sinh viên")

ten_sinh_vien = []
for hs in ds_sinh_vien:
    ten_sinh_vien.append(hs[0])
ten_duoc_chon = st.selectbox(
    "Chọn sinh viên:",
    ten_sinh_vien
)
# Hiển thị thông tin sinh viên được chọn
for hs in ds_sinh_vien:
    if hs[0] == ten_duoc_chon:
        st.write("Họ tên:", hs[0])
        st.write("Điểm chuyên cần:", hs[1])
        st.write("Điểm giữa kỳ:", hs[2])
        st.write("Điểm cuối kỳ:", hs[3])
        st.write("Điểm tổng kết:", hs[4])
        st.write("Xếp loại:", hs[5])
# Vẽ biểu đồ cột
st.subheader("Biểu đồ điểm tổng kết")
ten = []
diem = []
for hs in ds_sinh_vien:
    ten.append(hs[0])
    diem.append(hs[4])
fig, ax = plt.subplots()
ax.bar(ten, diem)
ax.set_xlabel("Sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
ax.set_title("Điểm tổng kết của 10 sinh viên")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
st.pyplot(fig)
# Thông tin người tạo
st.markdown(
    "<p style='font-size:12px;'>Người tạo: Nguyễn Ngọc Tươi | MSSV: 036308067091</p>",
    unsafe_allow_html=True
)

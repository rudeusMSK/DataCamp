# tạo biểu đồ chưa có dữ liệu.
# step1:
import matplotlib.pyplot as plt

# step2: 
# tạo 2 đối tượng: hình và trục với lệnh
#  >>>  plt.subplots() không có tham số

fig, ax = plt.subplots()
# chạy chương trình: 
#   1. Cài đặt package matplotlib tại terminal gõ lệnh / hoặc cài và chạy trên máy ảo conda
#     matplotlib >>> pip install matplotlib

#   2. Sau khi cài đặt xong, nhấn (ctrl + shift + p)
#       >>> tìm từ khóa: python: select interpreter và chọn trình biên dịch python

#   3.  chạy chương trình python
#       lệnh >>> plt.Show() ko tham số 
#                      để hiển thị đồ thị. 
plt.show()

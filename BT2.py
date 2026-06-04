
# 1. Phân tích Input / Output
# Dữ liệu toàn cục: saving_accounts là một danh sách chứa các đối tượng dạng từ điển (dictionary). Mỗi dictionary gồm: account_id (str), customer_name (str), balance (int), term_months (int), interest_rate (float), và status (str).

# Chức năng 1 :

# Input: Danh sách saving_accounts.

# Output: In chuỗi thông tin chi tiết từng sổ, hoặc báo trống nếu danh sách rỗng.

# Chức năng 2 (Mở sổ mới):

# Input: account_id, customer_name, balance, term_months, interest_rate từ bàn phím.

# Output: Tạo dict mới với trạng thái mặc định "active". Báo lỗi nếu trùng mã, trống tên, hoặc số liệu nhập không hợp lệ.

# Chức năng 3 :

# Input: account_id cần tìm và các thông tin mới cần sửa.

# Output: Ghi đè các giá trị mới vào dict của tài khoản đó. Chặn nếu tài khoản đã "closed".

# Chức năng 4 :

# Input: account_id cần tất toán.

# Output: Đổi trường status từ "active" sang "closed".

# Chức năng 5 :

# Input: account_id.

# Output: Tính và hiển thị Số tiền lãi và Tổng tiền nhận khi đáo hạn theo công thức.

# Chức năng 6 :

# Input: account_id và số tháng thực gửi.

# Output: So sánh thời gian thực gửi để áp dụng lãi suất phạt 0.5% hoặc lãi suất gốc, sau đó tính toán số tiền thực nhận.

# 2. Phương pháp bẫy dữ liệu bằng công cụ cơ bản
# Để xử lý việc người dùng nhập chữ vào các ô yêu cầu số mà không làm crash (sập) chương trình, ta áp dụng cơ chế kiểm tra chuỗi văn bản trước khi chuyển kiểu dữ liệu (int() hoặc float()):

# Đối với Số nguyên dương (Số tiền gửi, Kỳ hạn, Số tháng thực gửi):

# Dùng .isdigit(). Chuỗi hợp lệ chỉ chứa ký tự số (ví dụ: "50000000"). Nếu là số âm (có dấu "-"), số thập phân (có dấu ".") hoặc chữ cái, .isdigit() trả về False ngay lập tức.

# Sau khi .isdigit() xác nhận là True,  chuyển kiểu int(), sau đó kiểm tra điều kiện > 0 
# Lãi suất có thể là số thập phân như 6.5, do đó không dùng .isdigit() trực tiếp được 
# Giải pháp: Ta kiểm tra xem chuỗi nhập vào có chứa tối đa một dấu chấm hay không và phần còn lại có phải là số hay không. Hoặc đơn giản hơn: loại bỏ dấu chấm đầu tiên bằng phương thức .replace(".", "", 1). Nếu chuỗi sau khi loại bỏ dấu chấm đó là chuỗi số (.isdigit()), thì chuỗi gốc chính là một số thực hợp lệ.

# Sau khi chuyển đổi sang float(), tiếp tục kiểm tra điều kiện để đảm bảo số đó lớn hơn 0.

# ==============================================================================
# KHỞI TẠO DỮ LIỆU MẪU BAN ĐẦU
# ==============================================================================
saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")
    print("=========================================================")
    
    choice = input("Nhập lựa chọn của bạn (1-7): ").strip()
    
   
    if choice == "1":
        if len(saving_accounts) == 0:
            print("\nDanh sách sổ tiết kiệm hiện đang trống")
            continue
            
        print("\nDanh sách sổ tiết kiệm:")
        stt = 1
        for account in saving_accounts:
            print(f"{stt}. Mã sổ: {account['account_id']} | "
                  f"Khách hàng: {account['customer_name']} | "
                  f"Số tiền gửi: {account['balance']} | "
                  f"Kỳ hạn: {account['term_months']} tháng | "
                  f"Lãi suất: {account['interest_rate']}%/năm | "
                  f"Trạng thái: {account['status']}")
            stt += 1


    elif choice == "2":
        print("\n--- MỞ SỔ TIẾT KIỆM MỚI ---")
        
 
        input_id = input("Nhập mã sổ tiết kiệm: ").replace(" ", "").upper()
        if input_id == "":
            print("[LỖI] Mã sổ tiết kiệm không được để trống!")
            continue
            
       
        is_duplicate = False
        for account in saving_accounts:
            if account["account_id"] == input_id:
                is_duplicate = True
                break
        if is_duplicate:
            print("Mã sổ tiết kiệm đã tồn tại!")
            continue
            
     
        input_name = input("Nhập tên khách hàng: ").strip()
        if input_name == "":
            print("Tên khách hàng không được để trống")
            continue
            
  
        input_balance = input("Nhập số tiền gửi: ").strip()
        if not input_balance.isdigit():
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue
        balance_num = int(input_balance)
        if balance_num <= 0:
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue
            
       
        input_term = input("Nhập kỳ hạn gửi theo tháng: ").strip()
        if not input_term.isdigit():
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue
        term_num = int(input_term)
        if term_num <= 0:
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue
            
       
        input_rate = input("Nhập lãi suất năm (%): ").strip()
  
        if not input_rate.replace(".", "", 1).isdigit():
            print("Lãi suất không hợp lệ!")
            continue
        rate_num = float(input_rate)
        if rate_num <= 0:
            print("Lãi suất không hợp lệ!")
            continue
            
      
        new_account = {
            "account_id": input_id,
            "customer_name": input_name,
            "balance": balance_num,
            "term_months": term_num,
            "interest_rate": rate_num,
            "status": "active"
        }
        saving_accounts.append(new_account)
        print(f"[THÀNH CÔNG] Đã mở thành công sổ tiết kiệm {input_id} cho khách hàng {input_name}.")

  
    elif choice == "3":
        print("\n--- CẬP NHẬT THÔNG TIN SỔ TIẾT KIỆM ---")
        input_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").replace(" ", "").upper()
        
       
        found_account = None
        for account in saving_accounts:
            if account["account_id"] == input_id:
                found_account = account
                break
                
     
        if found_account is None:
            print("Không tìm thấy mã sổ tiết kiệm!")
            continue
            
  
        if found_account["status"] == "closed":
            print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
            continue
            
       
        new_name = input("Nhập tên khách hàng mới: ").strip()
        if new_name == "":
            print("Tên khách hàng không được để trống")
            continue
            
        new_balance_str = input("Nhập số tiền gửi mới: ").strip()
        if not new_balance_str.isdigit():
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue
        new_balance = int(new_balance_str)
        if new_balance <= 0:
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue
            
        new_term_str = input("Nhập kỳ hạn mới theo tháng: ").strip()
        if not new_term_str.isdigit():
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue
        new_term = int(new_term_str)
        if new_term <= 0:
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue
            
        new_rate_str = input("Nhập lãi suất năm mới (%): ").strip()
        if not new_rate_str.replace(".", "", 1).isdigit():
            print("Lãi suất không hợp lệ!")
            continue
        new_rate = float(new_rate_str)
        if new_rate <= 0:
            print("Lãi suất không hợp lệ!")
            continue
    
        found_account["customer_name"] = new_name
        found_account["balance"] = new_balance
        found_account["term_months"] = new_term
        found_account["interest_rate"] = new_rate
        print(f"[THÀNH CÔNG] Đã cập nhật thông tin mới cho mã sổ {input_id}.")

    elif choice == "4":
        print("\n--- TẤT TOÁN SỔ TIẾT KIỆM ---")
        input_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").replace(" ", "").upper()
  
        found_account = None
        for account in saving_accounts:
            if account["account_id"] == input_id:
                found_account = account
                break
                
    
        if found_account is None:
            print("Không tìm thấy mã sổ tiết kiệm")
            continue
            
 
        found_account["status"] = "closed"
        print(f"[THÀNH CÔNG] Sổ tiết kiệm {input_id} đã được tất toán thành công (Trạng thái: closed).")

  
    elif choice == "5":
        print("\n--- TÍNH LÃI DỰ KIẾN KHI ĐẾN HẠN ---")
        input_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").replace(" ", "").upper()
        
        found_account = None
        for account in saving_accounts:
            if account["account_id"] == input_id:
                found_account = account
                break
                

        if found_account is None:
            print("Không tìm thấy mã sổ tiết kiệm")
            continue
            
  
        if found_account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán")
            continue
            
  
        interest = found_account["balance"] * found_account["interest_rate"] / 100 * found_account["term_months"] / 12
        total_payout = found_account["balance"] + interest
        
        print(f"--- Kết quả tính lãi dự kiến cho sổ {input_id} ---")
        print(f"Số tiền gốc gửi : {found_account['balance']:,} VND")
        print(f"Kỳ hạn gửi      : {found_account['term_months']} tháng (Lãi suất: {found_account['interest_rate']}%/năm)")
        print(f"Tiền lãi nhận được: {interest:,} VND")
        print(f"Tổng tiền nhận khi đến hạn: {total_payout:,} VND")


    elif choice == "6":
        print("\n--- KIỂM TRA ĐIỀU KIỆN RÚT TRƯỚC HẠN ---")
        input_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").replace(" ", "").upper()
        
        found_account = None
        for account in saving_accounts:
            if account["account_id"] == input_id:
                found_account = account
                break
                
        if found_account is None:
            print("Không tìm thấy mã sổ tiết kiệm")
            continue
            
   
        if found_account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán")
            continue
            

        input_actual_months = input("Nhập số tháng thực gửi: ").strip()
        if not input_actual_months.isdigit():
            print("Số tháng thực gửi không hợp lệ!")
            continue
        actual_months = int(input_actual_months)
        if actual_months <= 0:
            print("Số tháng thực gửi không hợp lệ!")
            continue
            
   
        if actual_months < found_account["term_months"]:
            applied_rate = 0.5
            loai_rut = "RÚT TRƯỚC HẠN (Áp dụng lãi suất phạt không kỳ hạn 0.5%/năm)"
        else:
            applied_rate = found_account["interest_rate"]
            loai_rut = "RÚT ĐÚNG HẠN HOẶC QUÁ HẠN (Áp dụng lãi suất gốc của sổ)"
            
   
        actual_interest = found_account["balance"] * applied_rate / 100 * actual_months / 12
        actual_total_payout = found_account["balance"] + actual_interest
        
        print(f"--- Kết quả kiểm tra rút tiền cho sổ {input_id} ---")
        print(f"Hình thức xử lý : {loai_rut}")
        print(f"Số tiền gốc gửi : {found_account['balance']:,} VND")
        print(f"Số tháng thực gửi: {actual_months} tháng (Lãi suất áp dụng: {applied_rate}%/năm)")
        print(f"Tiền lãi thực nhận: {actual_interest:,} VND")
        print(f"Tổng tiền thực nhận: {actual_total_payout:,} VND")

 
    elif choice == "7":
        print("\nCảm ơn bạn đã sử dụng hệ thống quản lý sổ tiết kiệm TechBank. Tạm biệt!")
        break

  
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
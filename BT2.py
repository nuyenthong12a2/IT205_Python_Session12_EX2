# PHẦN 1: PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP1. Phân tích Input / Output cho các chức năngChức năngInput (Kiểu dữ liệu)Output mong đợi (Dạng hiển thị)1. Xem danh sáchKhông cóChuỗi định dạng danh sách sổ hoặc thông báo "Danh sách sổ tiết kiệm hiện đang trống".2. Mở sổ mớiaccount_id (str), customer_name (str), balance (int), term_months (int), interest_rate (float).Thêm dictionary mới vào list hoặc thông báo lỗi cụ thể (trùng mã, trống tên, sai số...).3. Cập nhật sổaccount_id (str) và các thông tin mới tương tự chức năng 2.Ghi đè giá trị cũ trong dictionary tương ứng hoặc thông báo lỗi (không tồn tại, đã closed, dữ liệu sai...).4. Tất toánaccount_id (str)Thay đổi trường "status": "closed" của sổ tương ứng.5. Tính lãi dự kiếnaccount_id (str)In ra màn hình: Tiền lãi dự kiến và Tổng tiền nhận khi đến hạn (float/int).6. Kiểm tra rút trước hạnaccount_id (str), real_months (int)In ra màn hình: Lãi suất áp dụng, Tiền lãi thực nhận, Tổng tiền thực nhận dựa trên số tháng thực gửi.2. Đề xuất giải pháp xử lý dữ liệu và Edge CasesChuẩn hóa Mã sổ (account_id): Sử dụng phương thức .strip().upper() để loại bỏ khoảng trắng thừa và chuyển thành chữ hoa.Kiểm tra tên khách hàng: Sử dụng .strip() và kiểm tra độ dài nếu bằng 0 (chuỗi rỗng) thì báo lỗi.Bẫy ép kiểu dữ liệu số (try-except): Khi người dùng nhập Số tiền, Kỳ hạn, Lãi suất hay Số tháng thực gửi, hệ thống sử dụng cấu trúc try-except ValueError để bắt các trường hợp nhập chữ hoặc ký tự đặc biệt, đồng thời kết hợp điều kiện > 0 để chặn số âm/bằng không.Quản lý Trạng thái: Chỉ cho phép thực hiện các chức năng 3, 5, 6 khi status == "active".3. Thiết kế Thuật toán (Luồng chương trình chính)PlaintextBắt đầu vòng lặp vô hạn (While True):
#     Hiển thị Menu CLI (1-7)
#     Bắt lỗi nhập Menu (Nếu không phải số từ 1-7 -> Báo lỗi, quay lại Menu)
    
#     Nếu Lựa chọn == 1:
#         Nếu list rỗng -> Báo trống
#         Ngược lại -> Duyệt list và in theo định dạng định sẵn
        
#     Nếu Lựa chọn == 2:
#         Nhập account_id -> Chuẩn hóa -> Kiểm tra trùng trong list
#         Nhập customer_name -> Kiểm tra trống
#         Nhập balance, term_months, interest_rate -> Ép kiểu & Kiểm tra > 0
#         Nếu tất cả hợp lệ -> Append dictionary mới có {"status": "active"} vào list
        
#     Nếu Lựa chọn == 3, 4, 5, 6:
#         Nhập account_id -> Chuẩn hóa -> Tìm kiếm trong list
#         Nếu không tìm thấy -> Báo lỗi "Không tìm thấy mã sổ tiết kiệm"
#         Nếu tìm thấy:
#             Nếu Lựa chọn == 3 (Cập nhật):
#                 Kiểm tra status == "closed" -> Báo lỗi "Không thể thao tác..."
#                 Nhập và kiểm tra tính hợp lệ của các thông tin mới -> Cập nhật
#             Nếu Lựa chọn == 4 (Tất toán):
#                 Cập nhật status = "closed"
#             Nếu Lựa chọn == 5 (Tính lãi):
#                 Kiểm tra status == "closed" -> Báo lỗi
#                 Tính lãi theo công thức chuẩn -> Hiển thị kết quả
#             Nếu Lựa chọn == 6 (Rút trước hạn):
#                 Kiểm tra status == "closed" -> Báo lỗi
#                 Nhập real_months -> Kiểm tra tính hợp lệ (>0)
#                 So sánh real_months với term_months -> Áp dụng lãi suất -> Tính & Hiển thị
                
#     Nếu Lựa chọn == 7:
#         In lời chào kết thúc -> Thoát vòng lặp (Break)
# PHẦN 2: TRIỂN KHAI SOURCE CODE PYTHONDưới đây là đoạn code Python hoàn chỉnh, được thiết kế tối ưu, bám sát các bẫy dữ liệu đề bài đưa ra:Python
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

def find_account(account_id):
    """Hàm bổ trợ tìm kiếm sổ tiết kiệm theo mã sổ"""
    for account in saving_accounts:
        if account["account_id"] == account_id:
            return account
    return None

while True:
    # Hiển thị Menu CLI
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-7): ").strip()
    
    # Bẫy 8 — Menu Validation
    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
        continue
        
    # --- CHỨC NĂNG 1: XEM DANH SÁCH ---
    if choice == "1":
        if not saving_accounts:
            print("Danh sách sổ tiết kiệm hiện đang trống")
        else:
            print("Danh sách sổ tiết kiệm:")
            for index, acc in enumerate(saving_accounts, start=1):
                print(f"{index}. Mã sổ: {acc['account_id']} | Khách hàng: {acc['customer_name']} | "
                      f"Số tiền gửi: {acc['balance']} | Kỳ hạn: {acc['term_months']} tháng | "
                      f"Lại suất: {acc['interest_rate']}%/năm | Trạng thái: {acc['status']}")
                      
    # --- CHỨC NĂNG 2: MỞ SỔ TIẾT KIỆM MỚI ---
    elif choice == "2":
        account_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()
        
        # Bẫy 1 — Mở sổ tiết kiệm với mã bị trùng
        if find_account(account_id) is not None:
            print("Mã sổ tiết kiệm đã tồn tại!")
            continue
            
        customer_name = input("Nhập tên khách hàng: ").strip()
        # Bẫy 2 — Tên khách hàng bị bỏ trống
        if not customer_name:
            print("Tên khách hàng không được để trống")
            continue
            
        # Bẫy 3 — Số tiền gửi hoặc kỳ hạn không hợp lệ
        try:
            balance = int(input("Nhập số tiền gửi: "))
            term_months = int(input("Nhập kỳ hạn gửi theo tháng: "))
            if balance <= 0 or term_months <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
        except ValueError:
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue
            
        # Bẫy 4 — Lãi suất không hợp lệ
        try:
            interest_rate = float(input("Nhập lãi suất năm: "))
            if interest_rate <= 0:
                print("Lại suất không hợp lệ!")
                continue
        except ValueError:
            print("Lại suất không hợp lệ!")
            continue
            
        # Nếu tất cả hợp lệ, tiến hành thêm mới
        new_account = {
            "account_id": account_id,
            "customer_name": customer_name,
            "balance": balance,
            "term_months": term_months,
            "interest_rate": interest_rate,
            "status": "active"
        }
        saving_accounts.append(new_account)
        print(f"Mở sổ tiết kiệm {account_id} thành công!")

    # --- CHỨC NĂNG 3: CẬP NHẬT THÔNG TIN SỔ ---
    elif choice == "3":
        account_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()
        account = find_account(account_id)
        
        # Bẫy 5 — Kiểm tra mã sổ tồn tại
        if account is None:
            print("Không tìm thấy mã sổ tiết kiệm")
            continue
            
        # Bẫy 6 — Thao tác trên sổ đã tất toán
        if account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán")
            continue
            
        customer_name = input("Nhập tên khách hàng mới: ").strip()
        if not customer_name:
            print("Tên khách hàng không được để trống")
            continue
            
        try:
            balance = int(input("Nhập số tiền gửi mới: "))
            term_months = int(input("Nhập kỳ hạn mới theo tháng: "))
            if balance <= 0 or term_months <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
        except ValueError:
            print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
            continue
            
        try:
            interest_rate = float(input("Nhập lãi suất năm mới: "))
            if interest_rate <= 0:
                print("Lại suất không hợp lệ!")
                continue
        except ValueError:
            print("Lại suất không hợp lệ!")
            continue
            
        # Cập nhật thông tin sau khi kiểm tra hợp lệ
        account["customer_name"] = customer_name
        account["balance"] = balance
        account["term_months"] = term_months
        account["interest_rate"] = interest_rate
        print(f"Cập nhật thành công thông tin sổ {account_id}!")

    # --- CHỨC NĂNG 4: TẤT TOÁN SỔ TIẾT KIỆM ---
    elif choice == "4":
        account_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
        account = find_account(account_id)
        
        # Bẫy 5 — Kiểm tra mã sổ tồn tại
        if account is None:
            print("Không tìm thấy mã sổ tiết kiệm")
            continue
            
        account["status"] = "closed"
        print(f"Tất toán sổ tiết kiệm {account_id} thành công! Trạng thái chuyển sang 'closed'.")

    # --- CHỨC NĂNG 5: TÍNH LÃI DỰ KIẾN KHI ĐẾN HẠN ---
    elif choice == "5":
        account_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()
        account = find_account(account_id)
        
        # Bẫy 5 — Kiểm tra mã sổ tồn tại
        if account is None:
            print("Không tìm thấy mã sổ tiết kiệm")
            continue
            
        # Bẫy 6 — Thao tác trên sổ đã tất toán
        if account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán")
            continue
            
        # Tính toán theo công thức nghiệp vụ
        interest = account["balance"] * account["interest_rate"] / 100 * account["term_months"] / 12
        total_received = account["balance"] + interest
        
        print(f"--- Kết quả tính lãi dự kiến cho sổ {account_id} ---")
        print(f"Tiền gốc: {account['balance']} VND")
        print(f"Tiền lãi dự kiến: {interest:.2f} VND")
        print(f"Tổng tiền nhận khi đến hạn: {total_received:.2f} VND")

    # --- CHỨC NĂNG 6: KIỂM TRA ĐIỀU KIỆN RÚT TRƯỚC HẠN ---
    elif choice == "6":
        account_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()
        account = find_account(account_id)
        
        # Bẫy 5 — Kiểm tra mã sổ tồn tại
        if account is None:
            print("Không tìm thấy mã sổ tiết kiệm")
            continue
            
        # Bẫy 6 — Thao tác trên sổ đã tất toán
        if account["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán")
            continue
            
        # Bẫy 7 — Số tháng thực gửi không hợp lệ
        try:
            real_months = int(input("Nhập số tháng thực gửi: "))
            if real_months <= 0:
                print("Số tháng thực gửi không hợp lệ!")
                continue
        except ValueError:
            print("Số tháng thực gửi không hợp lệ!")
            continue
            
        # Xác định lãi suất áp dụng
        if real_months < account["term_months"]:
            applied_rate = 0.5  # Lãi suất không kỳ hạn cố định khi rút trước hạn
            note = "Rút trước hạn (Áp dụng lãi suất không kỳ hạn 0.5%/năm)"
        else:
            applied_rate = account["interest_rate"]
            note = "Đủ hoặc vượt kỳ hạn (Áp dụng lãi suất ban đầu của sổ)"
            
        # Tính toán theo công thức thực nhận
        actual_interest = account["balance"] * applied_rate / 100 * real_months / 12
        actual_total = account["balance"] + actual_interest
        
        print(f"--- Kết quả kiểm tra rút trước hạn cho sổ {account_id} ---")
        print(f"Tình trạng: {note}")
        print(f"Lại suất áp dụng: {applied_rate}%/năm")
        print(f"Tiền lãi thực nhận: {actual_interest:.2f} VND")
        print(f"Tổng tiền thực nhận: {actual_total:.2f} VND")

    # --- CHỨC NĂNG 7: THOÁT CHƯƠNG TRÌNH ---
    elif choice == "7":
        print("Cảm ơn bạn đã sử dụng hệ thống quản lý tài khoản tiết kiệm TechBank. Hẹn gặp lại!")
        break
# Tank Trouble - Python (Pygame)

Dự án game bắn tank 2D viết bằng **Python + Pygame**.
Game có menu chọn chế độ, bản đồ mê cung ngẫu nhiên và hệ thống AI (auto-target + tìm đường A*).

## 1. Tính năng chính

- 3 chế độ chơi:
  - **Zombie World**: 1 người chơi đấu với zombie spawn liên tục.
  - **Training**: 1 người chơi đấu với 1 bot tank.
  - **2 Players (1v1)**: 2 người chơi đấu đối kháng trên cùng máy.
- Bản đồ được chọn ngẫu nhiên từ 5 file mê cung trong `MAZEFOLDER`.
- Tự động nhắm mục tiêu (auto-targeting) cho player/enemy.
- Enemy sử dụng **A*** để tìm đường.
- Hiển thị số kill theo thời gian thực.
- Màn hình pause/game over với các lựa chọn Continue / Restart / Exit.

## 2. Yêu cầu môi trường

- Python 3.10+ (khuyên dùng 3.11)
- Pygame

## 3. Cài đặt

Từ thư mục dự án (thư mục chứa `main.py`):

```bash
pip install pygame
```

## 4. Chạy game

```bash
python main.py
```

Sau khi chạy, menu chính sẽ hiện 3 chế độ chơi:

- `ZOMBIE WORLD`
- `TRAINING`
- `2 PLAYERS`

## 5. Điều khiển

### Player 1

- Di chuyển: phím mũi tên `← ↑ ↓ →`
- Hướng bắn: tự động khóa mục tiêu gần/hợp lệ

### Player 2 (chỉ ở chế độ 2 PLAYERS)

- Di chuyển: `W A S D`
- Hướng bắn: tự động khóa mục tiêu

### Điều khiển giao diện

- Nhấn nút setting (góc trên phải) để mở menu pause.
- Trong pause/game over:
  - `CONTINUE` (nếu có)
  - `RESTART`
  - `EXIT`

## 6. Cấu trúc dự án

```text
Game_Python/
  main.py                # Entry point
  mainGUI.py             # Menu chính
  game.py                # Vòng lặp game + các mode chơi
  sprites.py             # Player, Enemy, Bullet, Zombie, Wall, Explosion
  astar.py               # Thuật toán A* cho AI di chuyển
  auto_target.py         # Tự động nhắm mục tiêu
  auto_respawn.py        # Logic hồi sinh/spawn
  GameStatistics.py      # Thống kê kill, tốc độ bắn, trạng thái chết
  pauseGUI.py            # Màn hình pause
  gameOverGUI.py         # Màn hình game over
  Button.py              # Component button
  show_kill.py           # Hiển thị kill
  setting.py             # Hằng số cấu hình, màu sắc, tài nguyên
  MAZEFOLDER/
    MAZE1.txt
    MAZE2.txt
    MAZE3.txt
    MAZE4.txt
    MAZE5.txt
  img/                   # Hình ảnh game
```

## 7. Ký hiệu bản đồ (MAZEFOLDER/*.txt)

Các file map dùng ký tự để biểu diễn đối tượng:

- `1`: tường
- `0`: ô trống
- `*`: vị trí spawn Player 1
- `-`: vị trí spawn Player 2 hoặc TankEnemy (tùy mode)
- `?`: vị trí spawn ngẫu nhiên (respawn/spawn zombie)

Lưu ý: kích thước bản đồ nên tương ứng lưới hiển thị để tránh lệch đối tượng.

## 8. Tuỳ biến nhanh

- Tốc độ người chơi, FPS, kích thước màn hình: chỉnh trong `setting.py`.
- Tốc độ đạn/tần suất bắn mặc định: `GameStatistics.py`.
- Tần suất spawn zombie/tank: `auto_respawn.py`.
- Hành vi AI tìm đường và khóa mục tiêu: `astar.py`, `auto_target.py`.

## 9. Một số lưu ý kỹ thuật

- Dự án sử dụng biến toàn cục `PLAYER`, `ENEMY` để quản lý thực thể đang sống.
- Khi đổi ảnh trong `img/`, cần giữ tên file hoặc cập nhật hằng trong `setting.py`.
- Nếu chạy lỗi không tìm thấy ảnh/map, hãy kiểm tra bạn đang chạy đúng thư mục gốc dự án.

## 10. Hướng phát triển gợi ý

- Thêm âm thanh, nhạc nền.
- Thêm nhiều loại enemy và boss.
- Bổ sung hệ thống vật phẩm (power-up).
- Thêm chế độ online hoặc LAN.
- Tạo file `requirements.txt` để cài nhanh dependencies.

---

Nếu muốn, mình có thể viết tiếp:

1. `requirements.txt`
2. bản README tiếng Anh
3. hướng dẫn đóng gói `.exe` bằng PyInstaller

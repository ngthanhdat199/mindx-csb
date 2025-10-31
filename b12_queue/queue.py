# Khai báo
# cú pháp: tên biến = [giá trị 1, giá trị 2, giá trị 3, ...]
queue = [1, 2, 3, 4, 5]

# Xem phần tử đầu tiên của hàng đợi
front = queue[0]
print("front =", front)

# Enqueue / append: thêm phần tử vào cuối hàng đợi
queue.append(6)
print("new queue =", queue)

# Dequeue / pop: loại bỏ phần tử ở đầu hàng đợi
front_dequeued = queue.pop(0)
print("dequeued front =", front_dequeued)
print("new queue =", queue)

# Kiểm tra hàng đợi có rỗng không
if len(queue) == 0:
    print("queue is empty")

# mp3_player = MP3Player()
# mp3_player.add_song("Song 1")
# mp3_player.add_song("Song 2")
# mp3_player.add_song("Song 3")

# mp3_player.play_song()  # Phát "Song 1"
# mp3_player.skip_song()  # Bỏ qua "Song 1" và phát "Song 2"

# mp3_player.play_song()  # Phát "Song 2"
# mp3_player.skip_song()  # Bỏ qua "Song 2" và phát "Song 3"

# mp3_player.play_song()  # Phát "Song 3"
# mp3_player.skip_song()  # Không có bài hát nào để phát

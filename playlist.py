# playlist.py

songs = []

def add_song():
    title = input("Tên bài hát: ").strip()
    artist = input("Tên ca sĩ: ").strip()
    try:
        duration = int(input("Thời lượng (giây): ").strip())
    except ValueError:
        print("Thời lượng phải là số nguyên!")
        return
    songs.append({"title": title, "artist": artist, "duration": duration})
    print(f"Đã thêm bài hát: {title} - {artist} ({duration}s)")

def view_playlist():
    if not songs:
        print("Playlist hiện đang trống.")
        return
    print("\n--- PLAYLIST ---")
    for idx, song in enumerate(songs, 1):
        print(f"{idx}. {song['title']} - {song['artist']} ({song['duration']}s)")

def search_by_artist():
    artist_name = input("Nhập tên ca sĩ: ").strip().lower()
    results = [s for s in songs if artist_name in s['artist'].lower()]
    if not results:
        print(f"Không tìm thấy bài hát của '{artist_name}'.")
        return
    print(f"\nKết quả tìm kiếm ({len(results)}):")
    for s in results:
        print(f"- {s['title']} - {s['artist']} ({s['duration']}s)")

def main():
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")
        choice = input("Chọn chức năng: ").strip()

        if choice == '1':
            add_song()
        elif choice == '2':
            view_playlist()
        elif choice == '3':
            search_by_artist()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ hoặc chức năng chưa triển khai.")

if __name__ == "__main__":
    main()

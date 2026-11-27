
import os
import re
import json

# ==========================================
# CẤU HÌNH Tự tạo file stories.json  
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, "truyen.json")

# Nhận diện file Chuong_[số].txt
CHAPTER_PATTERN = re.compile(
    r"^Chuong_(\d+)\.txt$",
    re.IGNORECASE
)


# ==========================================
# ĐỌC NỘI DUNG CHƯƠNG
# ==========================================

def read_chapter(file_path):
    with open(file_path, "r", encoding="utf-8-sig") as file:
        content = file.read()

    # Chuẩn hóa xuống dòng Windows / Linux
    content = content.replace("\r\n", "\n")
    content = content.replace("\r", "\n")

    # Xóa khoảng trắng thừa ở đầu và cuối
    content = content.strip()

    return content


# ==========================================
# XỬ LÝ TỪNG BỘ TRUYỆN
# ==========================================

def process_story(folder_path):

    story_title = os.path.basename(folder_path)

    chapters = []

    # Lấy danh sách file chương
    chapter_files = []

    for filename in os.listdir(folder_path):

        match = CHAPTER_PATTERN.match(filename)

        if match:
            chapter_number = int(match.group(1))

            chapter_files.append(
                (chapter_number, filename)
            )

    # Sắp xếp theo số chương
    chapter_files.sort(key=lambda x: x[0])

    # Đọc từng chương
    for chapter_number, filename in chapter_files:

        file_path = os.path.join(folder_path, filename)

        content = read_chapter(file_path)

        chapters.append({
            "title": f"Chương {chapter_number}",
            "content": content
        })

    return {
        "title": story_title,
        "chapters": chapters
    }


# ==========================================
# QUÉT TẤT CẢ THƯ MỤC TRUYỆN
# ==========================================

def main():

    all_stories = []

    for folder_name in sorted(os.listdir(BASE_DIR)):

        folder_path = os.path.join(BASE_DIR, folder_name)

        # Chỉ xử lý thư mục
        if not os.path.isdir(folder_path):
            continue

        # Bỏ qua các thư mục không chứa file chương
        if not any(
            CHAPTER_PATTERN.match(f)
            for f in os.listdir(folder_path)
        ):
            continue

        story = process_story(folder_path)

        all_stories.append(story)

        print(
            f"Đã xử lý: {folder_name} "
            f"({len(story['chapters'])} chương)"
        )

    # ======================================
    # XUẤT FILE JSON
    # ======================================

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:

        json.dump(
            all_stories,
            file,
            ensure_ascii=False,
            indent=2
        )

    print("\n================================")
    print("HOÀN THÀNH CHUYỂN ĐỔI!")
    print(f"Tổng số bộ truyện: {len(all_stories)}")
    print(f"File xuất: {OUTPUT_FILE}")
    print("================================")


if __name__ == "__main__":
    main()

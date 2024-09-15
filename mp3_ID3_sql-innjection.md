# SQL Injection via MP3 Metadata

This document explains how to exploit an SQL injection vulnerability in the metadata of an MP3 file, which can affect fields such as `author_name`, `title`, and `ID` stored in the database.

## Exploitation Steps

1. **Identify the Vulnerability:**
   - The server stores MP3 metadata (e.g., `author_name`, `title`, `ID`) in a database. If the application does not properly sanitize these fields, SQL injection may be possible.

2. **Tool Used:**
   - **`id3v2`**: A tool used to modify ID3 tags in MP3 files, which include metadata like the author's name.

3. **Craft the Payload:**
   ```sh
   - id3v2 -a "$(xxd -l16 -ps /dev/urandom)', DATABASE() ) -- -" file_name.mp3 | curl -X POST -F "audio=@file_name.mp3" "URL" -L -s 

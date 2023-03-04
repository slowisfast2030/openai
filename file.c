#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file;
    char *filename = "file.txt";
    char line[256];  // 定义一个长度为256的字符数组用于存储每行读取到的内容
    int line_number = 1;  // 行号从1开始
    
    // 打开文件
    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Failed to open file: %s\n", filename);
        exit(1);
    }
    
    // 读取文件内容（按行）
    while (fgets(line, sizeof(line), file)) {
        // 输出行号和每行内容
        printf("Line %3d: %s", line_number, line);
        line_number++;
    }
    
    // 关闭文件
    fclose(file);
    return 0;
}

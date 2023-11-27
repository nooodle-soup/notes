# Mastering the Grep Command in Linux

## Introduction to Grep

Definition: grep (Global Regular Expression Print) is a versatile command-line 
utility in Linux primarily used for searching and extracting patterns from text
files. It employs regular expressions to define search patterns, making it a
powerful tool for text processing.

## Basic Usage

### 1. Search for a Pattern in a File:
```bash
grep "pattern" filename
```

### 2. Search for a Pattern in Multiple Files:
```bash
grep "pattern" file1.txt file2.txt
```

## Common Options

### 3. Ignore Case Distinctions:
```bash
grep -i "pattern" filename
```

### 4. Show Line Numbers:
```bash
grep -n "pattern" filename
```

### 5. Invert Match (Show Non-Matching Lines):
```bash
grep -v "pattern" filename
```

### 6. Recursive Search in Subdirectories:
```bash
grep -r "pattern" /path/to/directory
```

### 7. Basic Regex:
```bash
grep "^pattern" filename
```

### 8. Display N Lines Before and After:
```bash
grep -C 2 "pattern" filename
```

### 9. Count the Number of Lines Matching a Pattern:
```bash
grep -c "pattern" filename
```

### 10. Search for Multiple Patterns Using OR:
```bash
grep "pattern1\|pattern2" filename
```

### 11. Display Line Numbers Alongside Matching Lines:
```bash
grep -n "pattern" filename
```

### 12. Search for Whole Words Only:
```bash
grep -w "word" filename
```

## Advanced Usage

### 13. Files Containing a Specific Pattern:
```bash
find /path/to/search -type f -exec grep -l "pattern" {} +
```

### 14. Find and Replace Text in Files:
```bash
grep -rl "old_pattern" /path/to/search | xargs sed -i 's/old_pattern/new_pattern/g'
```

### 15. Search for a Pattern in Compressed Files:
```bash
zgrep "pattern" filename.gz
```

### 16. Recursive Search in Directories with Exclusions:
```bash
grep -r "pattern" --exclude=*.log --exclude-dir=exclude_folder /path/to/directory
```

### 17. Piping Output to Another Command
```bash
grep "404" access.log | awk '{print $7}' | sort | uniq -c | sort -rn
```

## Tips and Tricks

### 18. Colorize Output:
```bash
grep --color=auto "pattern" filename
```

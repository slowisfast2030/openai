#!/bin/bash

quick_sort() {
    local arr=("$@")
    local left=()
    local right=()
    local pivot="${arr[0]}"

    for i in "${arr[@]:1}"; do
        if (( i < pivot )); then
            left+=("$i")
        else
            right+=("$i")
        fi
    done

    if (( ${#left[@]} > 1 )); then
        left=($(quick_sort "${left[@]}"))
    fi

    if (( ${#right[@]} > 1 )); then
        right=($(quick_sort "${right[@]}"))
    fi

    printf '%s\n' "${left[@]}" "$pivot" "${right[@]}"
}

# 示例输入
input=(4 2 8 7 1 6 5 3)
result=($(quick_sort "${input[@]}"))

echo "Input Array: ${input[@]}"
echo "Sorted Array: ${result[@]}"

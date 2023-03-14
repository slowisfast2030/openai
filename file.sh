
#!/bin/bash
# set the shell to use bash as the interpreter

quick_sort() {
    # define a function called quick_sort taking an array as argument

    local arr=("$@")
      # create a new array variable called arr and assign it the values passed as arguments to the function

    local left=()
    local right=()
    local pivot="${arr[0]}"
      # create two new empty array variables called left and right, and create a new variable called pivot and assign it the first element in the arr array.

    for i in "${arr[@]:1}"; do
      # loop through all elements starting from the second one in the arr array

        if (( i < pivot )); then
          # if the current element is less than the pivot element, add the current element to the left array

            left+=("$i")
        else
          # else, add the current element to the right array

            right+=("$i")
        fi
    done

    if (( ${#left[@]} > 1 )); then
      # if the left array has more than one element, recursively call this function on the left array and update its value

        left=($(quick_sort "${left[@]}"))
    fi

    if (( ${#right[@]} > 1 )); then
      # if the right array has more than one element, recursively call this function on the right array and update its value

        right=($(quick_sort "${right[@]}"))
    fi

    printf '%s\n' "${left[@]}" "$pivot" "${right[@]}"
    # print the contents of the left array, followed by the pivot element, followed by the contents of the right array.
}

# Declare a new array called input with values 4 2 8 7 1 6 5 3
input=(4 2 8 7 1 6 5 3)

# Call the quick_sort function on the input array and assign the result to a new array called result.
result=($(quick_sort "${input[@]}"))

# Print the input array
echo "Input Array: ${input[@]}"

# Print the sorted result array 
echo "Sorted Array: ${result[@]}"

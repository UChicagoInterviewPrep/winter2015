#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define INITIAL 10

typedef struct
{
  int size;
  int cur_index;
  int *contents;
} arraylist;

arraylist *gen_array(void)
{
  arraylist *new_array = (arraylist *) malloc(sizeof(arraylist));
  int *contents = (int *) malloc(sizeof(int) * INITIAL);
  new_array->contents = contents;
  new_array->cur_index = 0;
  new_array->size = INITIAL;
  return new_array;
}

void resize_array(arraylist *arr, int newsize)
{
  int *new_contents = (int *) malloc(sizeof(int) * newsize);
  int i = 0;
  
  for (i = 0; i < arr->size; i++) {
    new_contents[i] = arr->contents[i];
  }
  arr->size = newsize;
  arr->contents = new_contents;
}

void add_num(arraylist *arr, int num)
{
  if (arr->size <= arr->cur_index) {
    resize_array(arr, arr->size * 2);
  }
  arr->contents[arr->cur_index] = num;
  arr->cur_index++;    
}

int main()
{
  arraylist *arr = gen_array();
  int j;
  for (j = 0; j < 40; j++) {
    add_num(arr, j);
  }

  for (j = 0; j < 40; j++) {
    printf("%d ", arr->contents[j]);
  }
  printf("\n");

  for (j = 0; j < 40; j++) {
    assert(arr->contents[j] == j);
  }

  return 0;
}

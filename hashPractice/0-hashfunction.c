#include <stdio.h>
#include <stdlib.h>
#define CAPACITY 50000

//define a hash table itme
typedef struct Ht_item{
    char* key;
    char* value;
}Ht_item;


//hash table has an array of pointers that pint ot Ht_itm
//define hash talbe
typedef struct HashTable
{
    // Contains an array of pointers to items.
    Ht_item** items;
    int size;  //size of the hash table
    int count; //number of elements
} HashTable;

//hash function
unsigned long hash_function(char* str){
    unsigned long i = 0;
    for (int j = 0; str[j]; j++){
        i += str[j];
    }
    return i % CAPACITY;
}

//create functions for allocating memory and creating items
//create  items by allocating memory for a key and value and 
//return a pointer to item
Ht_item* create_item(char* key, char* value)
{
    //create a pointer to a new HashTable item.
    Ht_item* item =(Ht_item*)malloc(sizeof(Ht_item));

    item->key = (char*) malloc(strlen(key) + 1);
    item->key = (char*) malloc(strlen(value)+ 1);
    strcpy(item->key, key);
    strcpy(item->value, value);
    return item;

}
//Create the table by allocating memory and setting size, count, and items:
HashTable* create_table(int size){
    //create a new HashTable
    HashTable* table = (HashTable*)malloc(sizeof(HashTable));
    table->size =size;
    table->count = 0;
    table->items= (Ht_item**)calloc(table->size, sizeof(Ht_item*));

    for (int i = 0; i <table->size; i++){
        table->items[i] = NULL;
    }

    return table;

}

void free_item(Ht_item* item)
{
    free(item->key);
    free(item->value);
    free(item);
}
void free_table(HashTable* table){
    //frees the table
    for (int i = 0; i < table->size; i++)
    {
        Ht_item*  item= table->items[i];
        if (item != NULL){
            free_item(item);
        }
    }
    free(table->items);
    free(table);
}

void print_table(HashTable* table)
{
    printf("\nHash Table\n--------------------------\n");
    for (int i = 0; i < table->size; i++){
        if(table->items[i]){
            printf("Inex: %d, key: %s, value: %S", i, table->items[i]-> key, table->items[i]->value);
        }
    }
    printf("----------------------------------------\n\n");
}

//insert

int main()
{
    char key[5] = "Hel"; 
    printf("string %s is mapped to index : %lu\n", key, hash_function(key));
    return 0;
}
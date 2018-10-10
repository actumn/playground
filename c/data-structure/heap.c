#include <stdio.h>

#define MAX_ELEMENT 200

// max heap -> 최댓값은 항상 root에 있다. root를 O(1)에 접근 가능.
// heap은 항상 최댓값/최솟값을 획득/저장에 특화.
// codes from https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html

typedef struct {
    int key;
} element;

typedef struct {
    element heap[MAX_ELEMENT];
    int heap_size;
} HeapType;

// insert시에 최댓값 갱신의 여지가 있음
void insert_max_heap(HeapType *h, element item) {
    int i;
    i = ++(h->heap_size);

    // 트리를 거슬러 올라가며 부모 노드와 비교
    while(i != 1 && item.key > h->heap[i/2].key) {
        h->heap[i] = h->heap[i/2];
        i /= 2;
    }
    h->heap[i] = item;
}

// delete는 최댓값을 꺼낸다
element delete_max_heap(HeapType *h) {
    int parent, child;
    element root, last;

    root = h->heap[1]; // root
    last = h->heap[(h->heap_size)--]; // last
    parent = 1;
    child = 2;

    // root에서 꺼낼때 last를 root로 넣고, 자식을 순회하며 비교한다.
    // heap 순회
    while (child <= h->heap_size) {
        // 두 child 중 더 큰 child를 찾는다.
        if (child < h->heap_size && h->heap[child].key < h->heap[child+1].key) {
            child++;
        }

        // last가 더 클 경우 더 할일은 없음.
        if (last.key >= h->heap[child].key) {
            break;
        }

        // last와 큰 child를 swap.
        h->heap[parent] = h->heap[child];
        // 한 단계 아래로
        parent = child;
        child *= 2;
    }

    h->heap[parent] = last;
    return root;
}


// heap정렬이 가장 유용할 때는 가장 큰 값 몇개만 필요할 때.
void heap_sort(element a[], int n) {
    HeapType heap;
    heap.heap_size = 0;

    int i = 0;
    for (i = 0; i < n; i++) {
        insert_max_heap(&heap, a[i]);
    }

    for (i = 0; i < n; i++) {
        a[i] = delete_max_heap(&heap);
    }
}


int main(int argc, char **argv) {
    HeapType heap;
    heap.heap_size = 0;

    element elem1, elem2, elem3, elem4, elem5;
    elem1.key = 5;
    elem2.key = 2;
    elem3.key = 8;
    elem4.key = 7;
    elem5.key = 9;

    insert_max_heap(&heap, elem1);
    insert_max_heap(&heap, elem2);
    insert_max_heap(&heap, elem3);
    insert_max_heap(&heap, elem4);
    insert_max_heap(&heap, elem5);
/*
    printf("%d\n", delete_max_heap(&heap).key);
    printf("%d\n", delete_max_heap(&heap).key);
    printf("%d\n", delete_max_heap(&heap).key);
    printf("%d\n", delete_max_heap(&heap).key);
    printf("%d\n", delete_max_heap(&heap).key);
*/
    element a[5];
    a[0] = elem1;
    a[1] = elem2;
    a[2] = elem3;
    a[3] = elem4;
    a[4] = elem5;
    heap_sort(a, 5);

    for (int i = 0; i < 5; i ++) {
        printf("%d\n", a[i].key);
    }

    return 0;
}

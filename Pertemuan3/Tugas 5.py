class NodeDLL:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = NodeDLL(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

# --- Jalankan Latihan 3 ---
dll = DoublyLinkedList()
print("=== LATIHAN 3: SEARCH DOUBLY LINKED LIST ===")
data_in = input("Masukkan elemen ke dalam Doubly Linked List: ") # Contoh: 2, 6, 9, 14, 20
for item in data_in.split(','):
    dll.append(int(item.strip()))

cari = int(input("Masukkan elemen yang ingin dicari: "))
if dll.search(cari):
    print(f"Elemen {cari} ditemukan dalam Doubly Linked List.")
else:
    print(f"Elemen {cari} tidak ditemukan.")

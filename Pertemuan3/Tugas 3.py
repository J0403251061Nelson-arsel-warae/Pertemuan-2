class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Tambah data ke akhir (Append)
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # LATIHAN 3: Fungsi Pencarian (Search)
    def search(self, key):
        current = self.head
        index = 0
        while current:
            if current.data == key:
                return index
            current = current.next
            index += 1
        return -1

    # LATIHAN 1: Fungsi Penghapusan (Delete)
    def delete_node(self, key):
        curr = self.head

        while curr:
            if curr.data == key:
                # Jika yang dihapus adalah Head
                if curr == self.head:
                    self.head = curr.next
                    if self.head:
                        self.head.prev = None
                else:
                    # Geser pointer next milik node sebelumnya
                    if curr.prev:
                        curr.prev.next = curr.next
                    # Geser pointer prev milik node sesudahnya
                    if curr.next:
                        curr.next.prev = curr.prev
                
                curr = None
                return True
            curr = curr.next
        return False

    # Fungsi untuk menampilkan list (Output)
    def display(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        print("Isi List saat ini: " + " <-> ".join(nodes) + " <-> None")

# --- INTERAKSI INPUT & OUTPUT ---

dll = DoublyLinkedList()

print("=== PROGRAM DOUBLY LINKED LIST LENGKAP ===")
# 1. Input Data Awal
raw_input = input("Masukkan elemen (pisahkan dengan koma, misal: 2,6,9,14,20): ")
list_data = [int(x.strip()) for x in raw_input.split(',')]
for d in list_data:
    dll.append(d)

dll.display()

# 2. Fitur Pencarian (Latihan 3)
target_cari = int(input("\nMasukkan elemen yang ingin DICARI: "))
indeks = dll.search(target_cari)
if indeks != -1:
    print(f"HASIL: Elemen {target_cari} ditemukan pada urutan ke-{indeks + 1}.")
else:
    print(f"HASIL: Elemen {target_cari} tidak ditemukan.")

# 3. Fitur Penghapusan (Latihan 1)
target_hapus = int(input("\nMasukkan elemen yang ingin DIHAPUS: "))
if dll.delete_node(target_hapus):
    print(f"HASIL: Elemen {target_hapus} berhasil dihapus.")
else:
    print(f"HASIL: Gagal menghapus, elemen {target_hapus} tidak ada.")

# Tampilan Akhir
print("\n--- Keadaan Akhir List ---")
dll.display()

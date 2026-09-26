## 5. Apa yang saya pelajari dari proses setup Git ini?
Yang saya pelajari dari proses ini adalah bagaimana sebuah komputer bisa berjalan dengan seimbang dengan kemampuan manusia yang terbatas jadi kesimpulannya adalah jika laptop saya tidak saya setup maka saya akan mencari filenya satu per satu dan itu sangat rumit dan melelahkan dan dengan adanya setup ini saya dapat mengubah atau menambahkan kode tanpa harus upload manual kedalam github alias mempermudah saya untuk melakukan maintenance dan update jika terjadi bug terhadap produk saya

## 6. Mengapa kita tidak bisa hanya copy-paste folder ke perangkat lain?
Untuk copypaste sendiri yang harus dilakukan adalah bagian git clone atau git pull dan database walaupun harus dicopy paste secara manual dan sisanya seperti File Environment (.env) dan Virtual Environment harus dibuat ulang karena agar user mengetahui bahwa sang developer sudah mengganti perangkat dengan yang baru yang pastinya membuat user merasa lebih aman dengan sistem keamanannya dan untuk File Log (.log) tidak perlu dilakukan perubahan karena file tersebut sudah bagian dari sistem kerja file yang kurang membutuhkan perawatan

## 7. Apa manfaat GitHub bagi startup?
Memudahkan developer untuk menguji file terbaru mereka melalui update file tanpa perlu sebar luaskan secara manual yang berulang contoh saya membuat file dan ingin update maka saya harus upload kedalam github yang otomatis menyebar kesemua perangkat user tanpa harus mengetik atau upload ulang file kode saya

## 8. Apa yang saya pelajari dari insiden file kosong ini?
saya mempelajari bahwa insiden file kosong adalah insiden yang sangat wajar terjadi diindustri it terutama koding aplikasi akan tetapi tidak boleh dianggap remeh karena kurangnya kode didalam file akan menentukan masa depan sebuah aplikasi 

## 9. Bagaimana cara menghindari kejadian serupa?
terutama jangan panik, gunakan refrensi lain seperti ai untuk mempelajari cara menanggulanginya dan harus melakukan backup secara fisik dan nonfisik agar kode didalam file tetap aman

## 10. Mengapa kita perlu backup fisik (flashdisk) selain GitHub?
melakukan backup fisik adalah hal yang sangat diharuskan agar menghindari kejadian seperti pengakuan tidak sah ataupun pencurian data pada intinya backup fisik dilakukan agar jika ada insiden pencurian data maka data asli tidak akan hilang

## 11. Mengapa `.env` tidak boleh di-commit ke GitHub?
karena file .env berisi kode rahasia sebuah aplikasi dan tidak boleh disebarluaskan agar menghindari plagiarisme dan pencurian data 

## 12. Apa yang harus dilakukan jika token sudah terlanjur ter-push?
harus melakukan revoke pada botfather atau lainnya untuk menonaktifkan kode token yang lama dan memperbarui kode token yang baru 

## 13. Apa yang saya pelajari hari ini tentang session di web?

session web berfungsi untuk memberikan tahapan pembangunan fondasi web untuk pemula terutama bagian login dan akun agar tidak mudah tersebar atau menjaga privasi

## 14. Apa perbedaan "dummy auth" dan "database auth"?

dummy auth: berfungsi sebagai data akun atau file pancingan untuk tes bug atau tes kompabilitas login
database auth: berfungsi sebagai data akun asli untuk implementasi langsung kode file data kedalam kompabilitas login

## 15. Apa yang masih membingungkan dari kode hari ini?

mungkin ada tetapi saya tidak tahu itu apa dan akan saya baca ulang nanti


## 16. Apa perbedaan dummy auth dan database auth?

dummy auth: sebagai autentikasi data palsu atau data umpan sebagai maintenance atau debugging
database auth: sebagai autentikasi data asli yang diubah menjadi kode unik dalam bentuk angka acak yang panjang agar data tetap aman dari duplikasi

## 17. Apa fungsi password hashing dan mengapa penting?

berfungsi mengubah password asli menjadi kode angka atau huruf acak yang panjang agar tidak ada duplikasi oleh oknum yang tidak bertanggug jawab dan sangat penting untuk menjaga data tetap privacy dan aman serta tidak bocor atau tersebar kesemua user

## 18. Bagaimana session menyimpan data admin yang login?

saya belum paham tentang hal ini

## 19. Apa yang masih membingungkan dari materi hari ini?

mungkin ada tetapi saya tidak tahu itu apa dan akan saya baca ulang nanti


## 20. Apa yang saya pelajari tentang CRUD hari ini?

CRUD singkatan dari Create Read Update Delete yang berfungsi sebagai tools bawaan untuk user yang akan membuat, membaca(cek perlengkapan), memperbarui data dan menghapus permanen pada data

## 21. Apa fungsi filter `tenant_id` di setiap query produk?

tenant_id berfungsi sebagai blokade antara data klien 1 dengan klien 2 agar tidak saling mengambil data satu sama lain

## 22. Kenapa hapus produk pakai POST, bukan GET?

memakai post cenderung lebih aman karena data tidak tersimpan pada website dan get sangat beresiko karena data user akan tersimpan kedalam bookmark atau cache yang memungkinkan deleting by human error

## 23. Apa bedanya "template universal" untuk tambah & edit?

template universal berfungsi sebagai DRY (Don't Repeat Yourself) yaitu tidak update ulang secara manual alias satu kali update semua akan baru

## 24. Apa yang masih membingungkan dari materi CRUD?

tidak ada
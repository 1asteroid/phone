// // Umumiy narxni saqlash uchun global o'zgaruvchini e'lon qilamiz
// let totalPrice = 0;
//
// // "Minus" tugmasi bosilganda miqdorni kamaytirish funksiyasi
// function decreaseQuantity() {
//     const inputElement = document.querySelector('.quantity input');
//     let quantity = parseInt(inputElement.value);
//     if (quantity > 1) {
//         quantity--;
//         inputElement.value = quantity;
//         calculateTotalPrice();
//     }
// }
//
// // "Plus" tugmasi bosilganda miqdorni oshirish funksiyasi
// function increaseQuantity() {
//     const inputElement = document.querySelector('.quantity input');
//     let quantity = parseInt(inputElement.value);
//     quantity++;
//     inputElement.value = quantity;
//     calculateTotalPrice();
// }
//
// // Umumiy narxni hisoblash va ko'rsatish funksiyasi
// function calculateTotalPrice() {
//     const pricePerItem = 10; // Har bir mahsulot uchun narx
//     const inputElement = document.querySelector('.quantity input');
//     const quantity = parseInt(inputElement.value);
//     totalPrice = pricePerItem * quantity;
//
//     // Umumiy narxni HTML-ga joylash
//     document.querySelector('.total-price span').textContent = totalPrice.toFixed(2);
// }
//
// // Minus tugmasini tanlangan paytda decreaseQuantity funksiyasini chaqirish
// document.querySelector('.btn-minus').addEventListener('click', decreaseQuantity);
//
// // Plus tugmasini tanlangan paytda increaseQuantity funksiyasini chaqirish
// document.querySelector('.btn-plus').addEventListener('click', increaseQuantity);
//
// // Sahifa yuklandi kema umumiy narxni hisoblash uchun calculateTotalPrice funksiyasini chaqirish
// document.addEventListener('DOMContentLoaded', calculateTotalPrice);

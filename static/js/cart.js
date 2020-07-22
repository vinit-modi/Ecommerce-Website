var updateBtns = document.getElementsByClassName('update-cart')

for(i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action )

        console.log('USER:', user)
        if (user === 'AnonymousUser') {
            console.log('User is not authenticated')
        }else {
            updateUserOrder(productId, action)
            }
        })
}

function updateUserOrder(productId, action){
    console.log('User is authenticated, sending data..')

    var url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })

    .then((response) =>{
        return response.json();
    })

    .then((data) =>{
        console.log('data:',data)
        location.reload()
    });
}

$(function() {
    $(document).click(function (event) {
      $('.navbar-collapse').collapse('hide');
    });
  });


var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
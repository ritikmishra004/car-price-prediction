async function predict(){

const data = {

brand: document.getElementById("brand").value,
fuel: document.getElementById("fuel").value,
seller_type: document.getElementById("seller").value,
transmission: document.getElementById("transmission").value,
owner: document.getElementById("owner").value,
km_driven: parseInt(document.getElementById("km").value),
car_age: parseInt(document.getElementById("age").value)

}

const response = await fetch("/predict",{

method:"POST",
headers:{
"Content-Type":"application/json"
},
body: JSON.stringify(data)

})

const result = await response.json()

document.getElementById("result").innerText =
"Estimated Price: ₹ " + result.predicted_price

}
function capvalid() {
  var Name = document.myform.name;
  var phoneNum = document.myform.mobile;
  var EmailId = document.myform.email;
  var emailExp = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([com\co\.\in])+$/; // to validate email id
  var City = document.myform.city;
  var Vehicle = document.myform.vehicle;
  var pass1 = document.myform.pwd;
  var pass2 = document.myform.cpwd;


  if (Name.value.length == "") {
    alert("Please Enter FullName");

    Name.focus();

    return false;
  }
  if (phoneNum.value.length > 10) {
    alert("Please Enter 10digit Contact Number");

    phoneNum.focus();

    return false;
  }
  if (phoneNum.value.length <= 0) {
    alert("Please Enter Correct Contact Number");

    phoneNum.focus();

    return false;
  }
  if (phoneNum.value.length <= 9) {
    alert("Please Enter Correct Contact Number");

    phoneNum.focus();

    return false;
  }

  if (City.value == '1') {

    alert("Please select the city");

    City.focus();

    return false;
  }

  if (Vehicle.value == 'Select Vehicle Type') {

    alert("Please select vehicle");

    Vehicle.focus();

    return false;
  }

  if (EmailId.value == '') {

    alert("Please Enter Email Id");

    EmailId.focus();

    return false;

}

if (EmailId.value != '') {

    if (!EmailId.value.match(emailExp)) {

        alert("Invalid Email Id");

        EmailId.focus()

        return false;

    }

  if (pass1.value =='') {
      alert('please enter the password');
      pass1.focus();

      return false;
  }

  if (pass2.value =='') {
      alert('please enter the password');
      pass2.focus();

      return false;
  }

}
  if (pass1.value != pass2.value) {
    alert("Mismatch Password");

    return false;
  }
}

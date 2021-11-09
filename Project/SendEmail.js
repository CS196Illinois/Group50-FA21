function sendEmail(user_email) {
    emailjs.send("service_e4bdf7a","template_fwtf2nk",{
        email: user_email,
        })
        .then(function (res) {
            console.log("success", res.status);
        });
}
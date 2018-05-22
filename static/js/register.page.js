const dataParser = data => {

    /*
        string to short
    */
    [
        'firstname',
        'lastname',
        'password',
        'repeatPassword',
    ].forEach( fieldname => {

        
        if (data[fieldname].trim().length < 4) {
            return {
                code: 1,
                value: fieldname,
            }
        } else {
            data[fieldname] = data[fieldname].trim()
        }
    })

    /*
        Passwords match
    */
    if (data['password'] !== data['repeatPassword']) {
        return {
        code: 2,
        value: 'password'
        }
    }



    return {code: 0}
}

$('form.form-signup').submit(function (event) {
    let data = {
        firstname: $('form.form-signup input#inputFirstname').val(),
        lastname: $('form.form-signup input#inputLastname').val(),
        password: $('form.form-signup input#inputPassword').val(),
        repeatPassword: $('form.form-signup input#inputRepeatPassword').val(),
    }

    const error =dataParser(data);
    if ( error.code != 0) {
        event.preventDefault();
    }


});
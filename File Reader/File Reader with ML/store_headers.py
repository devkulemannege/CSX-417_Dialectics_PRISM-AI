def colHeaders():
    '''stores column header presets'''

    colHeadersDict = {
        'nameHeaders' : ["name", "full_name", "fullname", "person_name", "contact_name",
                        "user_name", "customer_name", "employee_name", "client_name",
                        "Name", "Full_Name", "FullName", "Person_Name", "Contact_Name",
                        "User_Name", "Customer_Name", "Employee_Name", "Client_Name",
                        "name_full", "full name", "complete_name", "entire_name",
                        "Name (User)", "Employee Name", "Customer Name", "Contact Name",
                        "user_full_name", "customer_full_name", "person_full_name",
                        "name_full", "name_complete", "name_entire", "name_full_text",
                        "nameText", "nameString", "nameStr", "nameVal", "name_value",
                        "full_name_text", "full_name_string", "full_name_str", "full_name_val",
                        "primary_name", "initial_name", "display_name", "profile_name",
                        "registered_name", "contact_full_name", "user_full_name",
                        "user_profile_name", "customer_profile_name", "client_full_name", "customer"],

        'firstNameHeaders' : ["first_name", "firstname", "fname", "f_name", "name_first",
                            "firstName", "fName", "user_first_name", "customer_first_name",
                            "employee_first_name", "contact_first_name", "f_name", "fName",
                            "firstN", "given_name", "forename", "First Name", "First_Name", "Firstname", "Given Name", "FName",
                            "First", "First Name (User)", "Employee First Name", "Customer First Name","first_name", "firstName", "fname", "user_first_name", "customer_first_name",
                            "contact_first_name", "given_name", "primary_name", "initial_name","first_name", "firstname", "f_name", "FNAME", "FIRSTNAME", "F_NM",
                            "person_first_name", "user_first_name", "customer_first_name", "given_name", "primary_name", "first name", "Starting"],

        'lastNameHeaders' : ["last_name", "lastname", "lname", "l_name", "name_last",
                            "lastName", "lName", "user_last_name", "customer_last_name",
                            "employee_last_name", "contact_last_name", "l_name", "lName",
                            "lastN", "surname", "family_name", "last name",
                            "Last Name", "Last_Name", "Lastname", "Surname", "LName",
                            "Last", "Last Name (User)", "Employee Last Name", "Customer Last Name",
                            "last_name", "lastName", "lname", "user_last_name", "customer_last_name",
                            "contact_last_name", "surname", "family_name", "initial_last_name",
                            "last_name", "lastname", "l_name", "LNAME", "LASTNAME", "L_NM",
                            "person_last_name", "user_last_name", "customer_last_name", "surname", "family_name", "Ending"],

        'emailHeaders' : ["email", "email_address", "email_id", "user_email", "customer_email",
                        "contact_email", "email_address_1", "email_address_user", "emailAddr",
                        "emailAddress", "user_email_address", "primary_email", "secondary_email",
                        "Email", "Email_Address", "Email_ID", "User_Email", "Customer_Email",
                        "Contact_Email", "Email_Address_1", "Email_Address_User", "EmailAddr",
                        "EmailAddress", "User_Email_Address", "Primary_Email", "Secondary_Email",
                        "email", "emailAddress", "user_email", "customer_email", "contact_email",
                        "email_addr", "user_email_id", "primary_email_address", "secondary_email_address", "Email Address"],

        'mobileNumHeaders' : ["mobile_number", "mobile", "phone_number", "phone", "cell_number", 
                            "cell_phone", "user_mobile", "user_phone", "contact_number", "contact_phone",
                            "mobile_phone", "mobile_number_1", "mobile_number_user", "mobileNo",
                            "mobileNumber", "user_mobile_number", "primary_mobile", "secondary_mobile",
                            "Mobile_Number", "Mobile", "Phone_Number", "Phone", "Cell_Number",
                            "Cell_Phone", "User_Mobile", "User_Phone", "Contact_Number", "Contact_Phone",
                            "Mobile_Phone", "Mobile_Number_1", "Mobile_Number_User", "MobileNo",
                            "MobileNumber", "User_Mobile_Number", "Primary_Mobile", "Secondary_Mobile",
                            "mobile", "mobileNumber", "user_mobile", "contact_mobile", "mobile_number", 
                            "user_phone_number", "primary_mobile_number", "secondary_mobile_number","digit","Digit","Mobile Number", "num", "mobile no"],                                                   
    }
    return colHeadersDict

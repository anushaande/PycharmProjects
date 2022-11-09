#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("../Mail Merge Project/Input/Letters/starting_letter.txt") as starting_letter:
    invitation_text = starting_letter.read()
with open("../Mail Merge Project/Input/Names/invited_names.txt") as list_of_invitees:
    for name in list_of_invitees.readlines():
        personal_letter = invitation_text.replace("[name]", name.strip())
        with open(f"../Mail Merge Project/Output/ReadyToSend/letter_to_{name.strip()}.txt", mode="w") as invitation:
            invitation.write(personal_letter)




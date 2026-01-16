import segno
import shlex
import sys

def main():
    welcome_str = r"""                                                            
         
                                                       
 ▗▄▖ ▗▄▄▖   ▄▄  ▗▄▖ ▗▄ ▄▖▗▖    ▄▄▄ ▗▄ ▗▖▗▄▄▄▖  ▄▄ ▗▄▄▄▖▗▄ ▗▖
 █▀█ ▐▛▀▜▌ █▀▀▌ █▀█ ▐█ █▌▐▌    ▀█▀ ▐█ ▐▌▐▛▀▀▘ █▀▀▌▐▛▀▀▘▐█ ▐▌
▐▌ ▐▌▐▌ ▐▌▐▛   ▐▌ ▐▌▐███▌▐▌     █  ▐▛▌▐▌▐▌   ▐▌   ▐▌   ▐▛▌▐▌
▐▌ ▐▌▐███ ▐▌   ▐▌ ▐▌▐▌█▐▌▐▌     █  ▐▌█▐▌▐███ ▐▌▗▄▖▐███ ▐▌█▐▌
▐▌ ▐▌▐▌▝█▖▐▙   ▐▌ ▐▌▐▌▀▐▌▐▌     █  ▐▌▐▟▌▐▌   ▐▌▝▜▌▐▌   ▐▌▐▟▌
 █▄█▘▐▌ ▐▌ █▄▄▌ █▄█ ▐▌ ▐▌▐▙▄▄▖ ▄█▄ ▐▌ █▌▐▙▄▄▖ █▄▟▌▐▙▄▄▖▐▌ █▌
 ▝▀█ ▝▘ ▝▀  ▀▀  ▝▀▘ ▝▘ ▝▘▝▀▀▀▘ ▀▀▀ ▝▘ ▀▘▝▀▀▀▘  ▀▀ ▝▀▀▀▘▝▘ ▀▘
   ▝  
                ┳┓    ┳┓   ┓ ┏┓    
                ┣┫┓┏  ┣┫┓┏┏┣┓┏┛┏┓  
                ┻┛┗┫  ┻┛┗┻┗┛┗┗┛┛┗  
                   ┛                                                                              
                                                            """

    print(welcome_str)

    qr_gen()
    


def qr_gen():
    print("Please enter a Link to process:")
    url = input()
    #print("Please enter Directory to save the QR-Code:")
    #path = input()
    print("Please enter Name for the QR-Code:")
    name = input()
    print("Please enter Size")
    scale = input()


    qr_code = segno.make_qr(url)
    qr_code.save(
                name + ".png",
                scale = scale)

    print("Do you want to process another Link ? (y/n):")
    user_input = input()

    if user_input.lower() in ['y', "yes"]:
        qr_gen()
    else:
        sys.exit()

if __name__ == '__main__':
    sys.exit(main())

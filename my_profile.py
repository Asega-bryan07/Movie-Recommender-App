import streamlit as st
def app():
    # Path to the folder with images
    image_folder = 'profile/'

    # Profile image
    profile = image_folder + 'profile.jpg'
    profile_image = st.image(profile, caption='Developer', use_column_width=True)

    # QR code image
    qrcode_path = image_folder + 'qrcode.png'
    qrcode_image = st.image(qrcode_path, caption='GitHub: Asega-bryan07', use_column_width=True)

    # Additional information
    st.write("Contact me for more information:\n\n")

    # Social media links
    social_media_links = {
        'GitHub': 'https://github.com/Asega-bryan07',
        'LinkedIn': 'https://www.linkedin.com/in/almas-ibryan-07/',
        'Instagram': 'https://www.instagram.com/almas_ibryan/',
        'Twitter': 'https://twitter.com/almas_ibryan',
        'Facebook': 'https://www.facebook.com/almas.ibryan.3154',
        'Telegram': 'https://t.me/almasibryan',
        'Medium': 'https://medium.com/@almasibryan'
    }

    # icons for each social media platform
    icons = {
        'GitHub': 'fab fa-github',
        'LinkedIn': 'fab fa-linkedin',
        'Instagram': 'fab fa-instagram',
        'Twitter': 'fab fa-twitter',
        'Facebook': 'fab fa-facebook',
        'Telegram': 'fab fa-telegram',
        'Medium': 'fab fa-medium'
    }

    # Display social media links with icons
    st.write("Connect with me on social media")
    for platform, link in social_media_links.items():
        st.markdown(f"<i class='{icons[platform]}'></i> {platform}: [{link}]({link})", unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("Copyright © 2024 AI+|. All rights reserved.")

if __name__ == "__main__":
    app()

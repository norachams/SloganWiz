import streamlit as st
import cohere
import config

co = cohere.Client(config.api_key)


def create_gift(co, prompt):
    generation = co.generate(
        model='xlarge',
        prompt=prompt,
        max_tokens=15,
        temperature=1,
        stop_sequences=['\n','.']
    ).generations[0].text

    processed_generation = generation.split(":")[-1]
    st.header(processed_generation)

def main():
    st.set_page_config(page_title="PRESENT TIME", page_icon="👋")
    co = cohere.Client(config.api_key)
    prompt = """Generate a catchy slogan for a company named "[Company Name]" that specializes in 
    [Description of What the Company Does or Sells]. 
    The slogan should be memorable and reflect the essence or unique selling point of the company's products or services.

    Give all this, the slogan for a company named "EcoGlow Gardens" that specializes in sustainable gardening products should be: Where Sustainability Blooms.
    the slogan for a company named "Gourmet Delights" that offers high-end culinary experiences should be: Crafting Culinary Excellence.
    the slogan for a company named "AdventureGear Pro" that sells outdoor adventure equipment should be: Gear Up for Adventure.
    the slogan for a company named "TechGenius Solutions" that provides IT support and tech services should be: Your IT Experts in Action.
    the slogan for a company named "HealthyBite Snacks" that produces nutritious snack options. should be: Nourishing Your Well-being.

    the sloagn for COMPANY should be:"""
    st.title("🚀💡✨")

    giftee = st.text_input("Name of Company/Business", placeholder="HealthyBite Snacks")
    giftee_personality = st.text_input("What is Company/Business's description?", placeholder="Produces nutritious snack options")
    
    if giftee and giftee_personality:
        prompt = prompt.replace("COMPANY", giftee.strip())
        create_gift(co, prompt)

        _ = st.button("Another Sloagn  ")


if __name__ == "__main__":
    main()
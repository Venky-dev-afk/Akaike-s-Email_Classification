import gradio as gr
from utils import mask_pii
from models import predict_email_type

def classify_email(email_text):
    if not email_text.strip():
        return "No email provided.", "", ""

    # Step 1: Mask PII
    masked_email, pii_entities = mask_pii(email_text)

    # Step 2: Predict category
    prediction = predict_email_type(masked_email)

    return masked_email, ', '.join(pii_entities), prediction

with gr.Blocks() as demo:
    gr.Markdown("## 📧 Email Classification with PII Masking")
    with gr.Row():
        email_input = gr.Textbox(
            label="Enter Email Content", 
            placeholder="Type or paste an email here...", 
            lines=10
        )
    with gr.Row():
        submit_btn = gr.Button("Classify")
    
    with gr.Row():
        masked_output = gr.Textbox(label="Masked Email", lines=10)
    with gr.Row():
        entities_output = gr.Textbox(label="PII Entities")
        category_output = gr.Textbox(label="Predicted Category")

    submit_btn.click(
        fn=classify_email,
        inputs=[email_input],
        outputs=[masked_output, entities_output, category_output]
    )

demo.launch()

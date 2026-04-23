import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# 配置邮件账户
EMAIL_ADDRESS = "2691546385@qq.com"  # 替换为您的发送邮箱
EMAIL_PASSWORD = "aqlkvfxfgagydffi"  # 替换为您的SMTP授权码
SMTP_SERVER = "smtp.qq.com"  # 对于QQ邮箱
SMTP_PORT = 587
RECIPIENT_ADDRESS = "2691546385@qq.com"  # 替换为收件邮箱

# 模拟新闻数据
def fetch_news():
    return [
        {"category": "股市", "title": "美股三大指数上涨", "summary": "道指上涨1.2%，标普500上扬0.8%。", "url": "https://example.com/1"},
        {"category": "汇市", "title": "美元指数走强", "summary": "美元指数升至3个月高点。", "url": "https://example.com/2"},
        {"category": "AI", "title": "GPT-4再创新高", "summary": "OpenAI突破语言模型性能新极限。", "url": "https://example.com/3"},
    ]

# 生成HTML邮件内容
def generate_html_content(news_list):
    html_content = """
    <h1>每日新闻简报</h1>
    <p>以下是今天的重要新闻：</p>
    """
    for news in news_list:
        html_content += f"""
        <h3>类别: {news['category']}</h3>
        <ul>
            <li><b>标题:</b> <a href="{news['url']}">{news['title']}</a></li>
            <li><b>内容提要:</b> {news['summary']}</li>
        </ul>
        <hr>
        """
    return html_content

# 邮件发送逻辑
def send_email():
    news_list = fetch_news()
    html_content = generate_html_content(news_list)

    msg = MIMEText(html_content, "html", "utf-8")
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECIPIENT_ADDRESS
    msg["Subject"] = f"每日新闻简报 - {datetime.now().strftime('%Y-%m-%d')}"

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        print("邮件发送成功！")

if __name__ == "__main__":
    send_email()
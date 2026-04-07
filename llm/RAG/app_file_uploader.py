# 基于Streamlit完成WEB网页上传服务
import streamlit as st

st.title("📚 知识库更新服务")

uploaded_file = st.file_uploader(
    "请上传 TXT 文件",
    type=['txt'],
    accept_multiple_files=False
)

if uploaded_file is not None:
    file_name = uploaded_file.name
    file_type = uploaded_file.type
    file_size = uploaded_file.size / 1024

    st.subheader("📄 文件信息")
    st.write(f"文件名：{file_name}")
    st.write(f"格式：{file_type}")
    st.write(f"大小：{file_size:.2f} KB")

    # 读取文件内容
    try:
        content = uploaded_file.read().decode("utf-8")
    except UnicodeDecodeError:
        content = uploaded_file.read().decode("gbk", errors="ignore")

    st.subheader("📖 文件内容预览")
    st.text(content[:1000])  # 只展示前1000字符
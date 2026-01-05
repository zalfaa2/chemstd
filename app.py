import streamlit as st

st.set_page_config(page_title="Kalkulator Kimia", page_icon="🧪", layout="wide")

# =========================
# NAVIGASI DASHBOARD
# =========================
menu = st.sidebar.radio(
    "Pilih Dashboard",
    ["⚖️ Hitung Massa dari Konsentrasi", "💧 Pengenceran (C1V1=C2V2)"]
)

# =========================
# DASHBOARD 1: MASSA
# =========================
def page_massa():
    st.title("⚖️ Hitung Massa dari Konsentrasi")
    st.info("Ini dashboard perhitungan massa (yang Mr otomatis, ppm, %b/v, dll).")

    # 👉 Tempelkan kode kalkulator massamu di sini
    st.write("Tempelkan kode kalkulator massa kamu di sini...")

# =========================
# DASHBOARD 2: PENGENCERAN
# =========================
def page_pengenceran():
    st.title("💧 Kalkulator Pengenceran (C1V1 = C2V2)")
    st.write("Gunakan untuk menghitung volume/ konsentrasi saat pengenceran.")

    col1, col2 = st.columns(2)
    with col1:
        target = st.selectbox("Ingin mencari apa?", ["V1", "V2", "C1", "C2"])
        satuan_vol = st.selectbox("Satuan volume", ["mL", "L"])
    with col2:
        st.caption("Isi 3 nilai yang diketahui (satu yang dicari tidak perlu diisi).")

    # Input default
    C1 = st.number_input("C1 (konsentrasi awal)", min_value=0.0, format="%.4f")
    V1 = st.number_input(f"V1 ({satuan_vol}) (volume awal)", min_value=0.0, format="%.4f")
    C2 = st.number_input("C2 (konsentrasi akhir)", min_value=0.0, format="%.4f")
    V2 = st.number_input(f"V2 ({satuan_vol}) (volume akhir)", min_value=0.0, format="%.4f")

    if st.button("Hitung Pengenceran", use_container_width=True):
        try:
            if target == "V1":
                if C1 == 0:
                    raise ValueError("C1 tidak boleh 0")
                hasil = (C2 * V2) / C1
                st.success(f"✅ V1 = **{hasil:.4f} {satuan_vol}**")

            elif target == "V2":
                if C2 == 0:
                    raise ValueError("C2 tidak boleh 0")
                hasil = (C1 * V1) / C2
                st.success(f"✅ V2 = **{hasil:.4f} {satuan_vol}**")

            elif target == "C1":
                if V1 == 0:
                    raise ValueError("V1 tidak boleh 0")
                hasil = (C2 * V2) / V1
                st.success(f"✅ C1 = **{hasil:.4f}**")

            elif target == "C2":
                if V2 == 0:
                    raise ValueError("V2 tidak boleh 0")
                hasil = (C1 * V1) / V2
                st.success(f"✅ C2 = **{hasil:.4f}**")

            st.caption("Rumus: C1 × V1 = C2 × V2")

        except Exception as e:
            st.error(f"❌ Error: {e}")

# =========================
# ROUTING
# =========================
if menu == "⚖️ Hitung Massa dari Konsentrasi":
    page_massa()
else:
    page_pengenceran()

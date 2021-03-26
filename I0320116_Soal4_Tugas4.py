#syarat mendaftar kursus online


usia = int(input("masukkan usia"))
ujian = (input("masukkan lulus ujian atau tidak (Y/T)"))

if (usia>=21) and (ujian == "Y" ):
    print("anda boleh mendaftar kursus online ini")
else:
    print("anda tidak boleh mendaftar kursus online ini")
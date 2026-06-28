from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "products"


PRODUCTS = {
    "omega-3": {
        "name": "B2H Omega-3",
        "label_url": "https://wearenextgen.github.io/b2h-viewer/assets/labels/omega-3.png",
        "usage_images": [
            "https://wearenextgen.github.io/b2h-viewer/img/card-brain.jpg",
            "https://wearenextgen.github.io/b2h-viewer/img/heart-glass.jpg",
            "https://wearenextgen.github.io/b2h-viewer/img/eye-photo.jpg",
            "https://wearenextgen.github.io/b2h-viewer/img/card-triglycerides.jpg",
        ],
        "tagline": "Η καθημερινή δύναμη της καρδιάς, του εγκεφάλου και της όρασης.",
        "benefit_intro": "Τα Ωμέγα-3 λιπαρά οξέα αποτελούν έναν από τους σημαντικότερους συμμάχους της καθημερινής υγείας.",
        "micro_tagline": "Η καθημερινή φροντίδα που αξίζει ο οργανισμός σας.",
        "quality_intro": "Υψηλής ποιότητας Ωμέγα-3 λιπαρά οξέα για καθημερινή υποστήριξη.",
        "palette": ("#ddc4a0", "#d2eef5", "#755c49", "#c0954e"),
        "images": [
            "https://wearenextgen.github.io/b2h-viewer/img/card-brain.jpg",
            "https://wearenextgen.github.io/b2h-viewer/img/heart-glass.jpg",
            "https://wearenextgen.github.io/b2h-viewer/img/eye-photo.jpg",
            "https://wearenextgen.github.io/b2h-viewer/img/cell-gold.jpg",
            "https://wearenextgen.github.io/b2h-viewer/img/joint-clean.jpg",
            "https://wearenextgen.github.io/b2h-viewer/img/card-triglycerides.jpg",
        ],
        "image_cards": [
            ("Εγκέφαλος", "Το DHA συμβάλλει στη διατήρηση της φυσιολογικής λειτουργίας του εγκεφάλου."),
            ("Καρδιά", "Συμβάλλει στη φυσιολογική λειτουργία της καρδιάς μέσω των πολύτιμων λιπαρών οξέων EPA και DHA."),
            ("Όραση", "Το DHA συμβάλλει στη διατήρηση της φυσιολογικής όρασης."),
            ("Καθημερινή υποστήριξη", "Μια αξιόπιστη πηγή Ωμέγα-3 για έναν σύγχρονο τρόπο ζωής."),
            ("Premium ποιότητα", "Υψηλής ποιότητας Ωμέγα-3 λιπαρά οξέα EPA και DHA."),
            ("Τριγλυκερίδια", "Η σχετική πληροφορία παραμένει ενσωματωμένη στο εγκεκριμένο δημιουργικό της εικόνας."),
        ],
        "facts": [
            ("EPA & DHA", "Πολύτιμα πολυακόρεστα λιπαρά οξέα που συμμετέχουν σε σημαντικές φυσιολογικές λειτουργίες."),
            ("Καρδιά", "Τα EPA και DHA συμβάλλουν στη φυσιολογική λειτουργία της καρδιάς με ημερήσια πρόσληψη 250 mg EPA και DHA."),
            ("Εγκέφαλος", "Το DHA συμβάλλει στη διατήρηση της φυσιολογικής λειτουργίας του εγκεφάλου με ημερήσια πρόσληψη 250 mg DHA."),
            ("Όραση", "Το DHA συμβάλλει στη διατήρηση της φυσιολογικής όρασης με ημερήσια πρόσληψη 250 mg DHA."),
        ],
        "benefits": [
            "Φυσιολογική λειτουργία της καρδιάς",
            "Διατήρηση της φυσιολογικής λειτουργίας του εγκεφάλου",
            "Διατήρηση της φυσιολογικής όρασης",
            "Υψηλής ποιότητας EPA και DHA",
            "Υψηλή καθαρότητα πρώτης ύλης",
            "Καθημερινή χρήση",
        ],
        "benefit_icons": ["heart", "brain", "eye", "fish"],
        "benefit_tiles": [
            ("Καρδιά & κυκλοφορία", "Καθημερινή υποστήριξη της φυσιολογικής λειτουργίας της καρδιάς."),
            ("Εγκέφαλος & απόδοση", "Το DHA υποστηρίζει τη φυσιολογική λειτουργία του εγκεφάλου."),
            ("Όραση", "Το DHA συμβάλλει στη διατήρηση της φυσιολογικής όρασης."),
            ("Υψηλή καθαρότητα", "Premium Ωμέγα-3 λιπαρά οξέα για καθημερινή χρήση."),
        ],
        "why_intro": "Τα Ωμέγα-3 λιπαρά οξέα αποτελούν έναν από τους σημαντικότερους συμμάχους της καθημερινής υγείας. Το B2H Omega-3 προσφέρει υψηλής ποιότητας EPA και DHA για μια αξιόπιστη καθημερινή πηγή Ωμέγα-3.",
        "why_detail": "Η σύγχρονη διατροφή συχνά δεν καλύπτει επαρκώς τις ανάγκες σε Ωμέγα-3. Η καθημερινή συμπληρωματική πρόσληψη μπορεί να αποτελέσει σημαντικό μέρος μιας ολοκληρωμένης στρατηγικής ευζωίας και well-being.",
        "why_paragraphs": [
            "Το B2H Omega-3 προσφέρει υψηλής ποιότητας Ωμέγα-3 λιπαρά οξέα EPA και DHA, σχεδιασμένα για να υποστηρίζουν φυσιολογικές λειτουργίες του οργανισμού που επηρεάζουν την ποιότητα ζωής κάθε ημέρα.",
            "Η σύγχρονη διατροφή συχνά δεν καλύπτει επαρκώς τις ανάγκες σε Ωμέγα-3. Η καθημερινή συμπληρωματική πρόσληψη μπορεί να αποτελέσει σημαντικό μέρος μιας ολοκληρωμένης στρατηγικής ευζωίας και well-being.",
            "Τα EPA και DHA είναι απαραίτητα πολυακόρεστα λιπαρά οξέα που συμμετέχουν σε σημαντικές φυσιολογικές λειτουργίες του οργανισμού.",
            "Το B2H Omega-3 σχεδιάστηκε για όσους επιθυμούν μια αξιόπιστη καθημερινή πηγή Ωμέγα-3 υψηλής ποιότητας, ως μέρος ενός υγιεινού τρόπου ζωής και μιας ισορροπημένης διατροφής.",
            "Η συστηματική λήψη του μπορεί να αποτελέσει πολύτιμο σύμμαχο για τη συνολική ευζωία, υποστηρίζοντας φυσιολογικές λειτουργίες που σχετίζονται με την καρδιά, τον εγκέφαλο και την όραση.",
        ],
        "ingredients": [
            ("EPA", "Υψηλής ποιότητας EPA για καθημερινή μικροθρεπτική υποστήριξη."),
            ("DHA", "Υψηλής ποιότητας DHA για εγκέφαλο και όραση."),
            ("Καθαρότητα", "Υψηλή καθαρότητα πρώτης ύλης και ελεγχόμενη ποιότητα παραγωγής."),
            ("Clinical Formula", "Premium σύνθεση σχεδιασμένη για σταθερή καθημερινή χρήση."),
        ],
        "quality": [
            ("Υψηλής καθαρότητας Ωμέγα-3 λιπαρά οξέα", "Premium πρώτη ύλη για αξιόπιστη καθημερινή χρήση."),
            ("Υψηλής ποιότητας DHA", "Συστατικό με εγκεκριμένους ισχυρισμούς για εγκέφαλο και όραση."),
            ("Ελεγχόμενη ποιότητα παραγωγής", "Σταθερή ποιότητα παραγωγής για αξιόπιστη καθημερινή χρήση."),
            ("Premium Formula", "Στοχευμένη σύνθεση Ωμέγα-3 λιπαρών οξέων."),
        ],
        "ideal_for": [
            "Άτομα με απαιτητικό τρόπο ζωής",
            "Άνδρες και γυναίκες κάθε ηλικίας",
            "Άτομα που καταναλώνουν περιορισμένες ποσότητες λιπαρών ψαριών",
            "Άτομα που επιθυμούν καθημερινή υποστήριξη της καρδιαγγειακής υγείας",
            "Άτομα που αναζητούν ολοκληρωμένη στρατηγική ευζωίας",
        ],
        "stats": [("30", "Κάψουλες"), ("Υψηλή", "Καθαρότητα"), ("Daily", "Καθημερινή χρήση"), ("Premium", "Formula")],
        "usage": "Λαμβάνετε την προτεινόμενη ημερήσια δόση σύμφωνα με τις οδηγίες της συσκευασίας, κατά προτίμηση μαζί με κύριο γεύμα.",
        "usage_steps": [
            ("01", "Ελέγξτε τη δόση", "Ακολουθήστε την προτεινόμενη ημερήσια δόση της τελικής συσκευασίας."),
            ("02", "Μαζί με γεύμα", "Προτιμήστε τη λήψη μαζί με το κύριο γεύμα."),
            ("03", "Καθημερινή συνέπεια", "Η σταθερή καθημερινή χρήση αποτελεί το σημαντικότερο βήμα."),
        ],
        "usage_stat": ("30", "Κάψουλες"),
        "closing": ["Κάθε ημέρα φροντίζετε την καρδιά σας.", "Κάθε ημέρα φροντίζετε τον εγκέφαλό σας.", "Κάθε ημέρα επενδύετε στην ποιότητα ζωής σας."],
        "disclaimer": "Το EPA και το DHA συμβάλλουν στη φυσιολογική λειτουργία της καρδιάς με ημερήσια πρόσληψη 250 mg EPA και DHA. Το DHA συμβάλλει στη διατήρηση της φυσιολογικής λειτουργίας του εγκεφάλου και της φυσιολογικής όρασης με ημερήσια πρόσληψη 250 mg DHA. Το προϊόν είναι συμπλήρωμα διατροφής και δεν υποκαθιστά μια ισορροπημένη διατροφή και έναν υγιεινό τρόπο ζωής. Οι ισχυρισμοί βασίζονται αποκλειστικά στους εγκεκριμένους ισχυρισμούς υγείας της EFSA για τα Ωμέγα-3 λιπαρά οξέα EPA και DHA.",
    },
    "multivitamin": {
        "name": "B2H Multivitamin Complex",
        "label_url": "https://wearenextgen.github.io/b2h-viewer/assets/labels/multivitamin.png",
        "usage_images": ["", "", "", ""],
        "tagline": "Η καθημερινή βάση της υγείας σας.",
        "benefit_intro": "Μία ταμπλέτα. Δεκάδες πολύτιμα μικροθρεπτικά συστατικά. Κάθε ημέρα.",
        "micro_tagline": "Η δύναμη της κάθε ημέρας ξεκινά από μέσα.",
        "quality_intro": "Premium επιστημονικά σχεδιασμένη καθημερινή μικροθρεπτική υποστήριξη.",
        "palette": ("#f0cf73", "#dceef1", "#775b3f", "#c38d3d"),
        "images": ["", "", "", "", "", ""],
        "image_cards": [
            ("Καθημερινή ενέργεια", "Συμβάλλει στη φυσιολογική παραγωγή ενέργειας."),
            ("Λιγότερη κόπωση", "Συμβάλλει στη μείωση της κόπωσης και της εξάντλησης."),
            ("Ανοσοποιητικό", "Υποστηρίζει τη φυσιολογική λειτουργία του ανοσοποιητικού συστήματος."),
            ("Κυτταρική προστασία", "Προστατεύει τα κύτταρα από το οξειδωτικό στρες."),
            ("Οστά & μύες", "Υποστηρίζει τη φυσιολογική λειτουργία οστών και μυών."),
            ("Κάθε ημέρα", "Μία ταμπλέτα με δεκάδες πολύτιμα μικροθρεπτικά συστατικά."),
        ],
        "facts": [
            ("Ενέργεια", "Ο ισορροπημένος συνδυασμός βιταμινών και μετάλλων συμβάλλει στη φυσιολογική παραγωγή ενέργειας."),
            ("Άμυνα", "Υποστηρίζει τη φυσιολογική λειτουργία του ανοσοποιητικού συστήματος."),
            ("Προστασία", "Συμβάλλει στην προστασία των κυττάρων από το οξειδωτικό στρες."),
            ("Οστά & μύες", "Υποστηρίζει τη φυσιολογική λειτουργία οστών και μυών."),
        ],
        "benefits": [
            "Φυσιολογική παραγωγή ενέργειας",
            "Μείωση κόπωσης και εξάντλησης",
            "Φυσιολογική λειτουργία ανοσοποιητικού",
            "Προστασία από οξειδωτικό στρες",
            "Υποστήριξη οστών και μυών",
            "Καθημερινή χρήση για γυναίκες και άνδρες",
        ],
        "benefit_icons": ["bolt", "shield", "cell", "bone"],
        "benefit_tiles": [
            ("Ενέργεια", "Καθημερινή υποστήριξη του φυσιολογικού ενεργειακού μεταβολισμού."),
            ("Ανοσοποιητικό", "Μικροθρεπτικά συστατικά για τη φυσιολογική λειτουργία της άμυνας."),
            ("Κυτταρική προστασία", "Υποστήριξη απέναντι στο οξειδωτικό στρες."),
            ("Οστά & μύες", "Ολοκληρωμένη καθημερινή μικροθρεπτική υποστήριξη."),
        ],
        "why_intro": "Το B2H Multivitamin Complex δεν σχεδιάστηκε απλώς για να περιέχει πολλές βιταμίνες. Δημιουργήθηκε ως σταθερή καθημερινή βάση μικροθρεπτικής υποστήριξης για τον σύγχρονο τρόπο ζωής.",
        "why_detail": "Ένας ισορροπημένος συνδυασμός βιταμινών, μετάλλων και ιχνοστοιχείων υψηλής ποιότητας υποστηρίζει σημαντικές φυσιολογικές λειτουργίες του οργανισμού μέσα από μία μόνο καθημερινή ταμπλέτα.",
        "why_paragraphs": [
            "Ο σύγχρονος τρόπος ζωής, οι γρήγοροι ρυθμοί, το άγχος και οι διατροφικές ελλείψεις αυξάνουν καθημερινά τις ανάγκες του οργανισμού σε βιταμίνες και μέταλλα.",
            "Το B2H Multivitamin Complex δημιουργήθηκε για να αποτελεί τη σταθερή καθημερινή βάση μικροθρεπτικής υποστήριξης του οργανισμού, συμβάλλοντας στη φυσιολογική παραγωγή ενέργειας, στη σωστή λειτουργία του ανοσοποιητικού συστήματος και στην προστασία των κυττάρων από το οξειδωτικό στρες.",
            "Γιατί η πραγματική ευεξία δεν ξεκινά όταν εμφανιστεί το πρόβλημα. Ξεκινά κάθε πρωί.",
            "Το B2H Multivitamin Complex δεν σχεδιάστηκε απλώς για να περιέχει πολλές βιταμίνες.",
            "Σχεδιάστηκε ώστε να προσφέρει μια ολοκληρωμένη καθημερινή υποστήριξη στις φυσιολογικές λειτουργίες του οργανισμού, μέσα από έναν ισορροπημένο συνδυασμό βιταμινών, μετάλλων και ιχνοστοιχείων υψηλής ποιότητας.",
            "Η σύνθεσή του συμβάλλει στη φυσιολογική παραγωγή ενέργειας, στην εύρυθμη λειτουργία του νευρικού και ανοσοποιητικού συστήματος, στη διατήρηση υγιών οστών και μυών και στην προστασία των κυττάρων από το οξειδωτικό στρες.",
        ],
        "ingredients": [
            ("Βιταμίνες", "A, C, D3, E και πλήρες σύμπλεγμα βιταμινών Β."),
            ("Μέταλλα", "Μαγνήσιο, ασβέστιο, ψευδάργυρος, σελήνιο και σίδηρος."),
            ("Ιχνοστοιχεία", "Ιώδιο, χρώμιο, χαλκός και μαγγάνιο."),
            ("Εξειδικευμένα", "Βιοτίνη, φολικό οξύ και λουτεΐνη."),
        ],
        "quality": [
            ("Πλήρης σύνθεση", "Συνδυασμός βιταμινών, μετάλλων και ιχνοστοιχείων."),
            ("Ισορροπημένη φόρμουλα", "Σχεδιασμένη για ολοκληρωμένη καθημερινή υποστήριξη."),
            ("Μία ταμπλέτα", "Απλή καθημερινή χρήση χωρίς περίπλοκη ρουτίνα."),
            ("Premium ποιότητα", "Πρώτες ύλες υψηλής ποιότητας για καθημερινή χρήση."),
        ],
        "ideal_for": [
            "Άτομα με απαιτητικό τρόπο ζωής",
            "Εργαζόμενους με αυξημένες καθημερινές υποχρεώσεις",
            "Άτομα που αισθάνονται εύκολα κόπωση",
            "Γυναίκες και άνδρες που επιθυμούν καθημερινή μικροθρεπτική υποστήριξη",
            "Άτομα που επιδιώκουν ολοκληρωμένη στρατηγική ευζωίας",
        ],
        "stats": [("30", "Ταμπλέτες"), ("1", "Ταμπλέτα ημερησίως"), ("High", "Υψηλή ποιότητα")],
        "usage": "Λαμβάνετε 1 ταμπλέτα ημερησίως, κατά προτίμηση μαζί με το κύριο γεύμα.",
        "usage_steps": [
            ("01", "Μία ταμπλέτα", "Λαμβάνετε μία ταμπλέτα κάθε ημέρα."),
            ("02", "Με κύριο γεύμα", "Προτιμήστε τη λήψη μαζί με το κύριο γεύμα."),
            ("03", "Σταθερή ρουτίνα", "Η συστηματική καθημερινή λήψη υποστηρίζει τη μικροθρεπτική επάρκεια."),
        ],
        "usage_stat": ("1", "Ταμπλέτα ημερησίως"),
        "closing": ["Η καθημερινή σας επένδυση στην υγεία.", "Γιατί η ενέργεια, η άμυνα του οργανισμού και η ευζωία δεν είναι θέμα τύχης.", "Είναι αποτέλεσμα της σωστής καθημερινής φροντίδας."],
        "disclaimer": "Το προϊόν είναι συμπλήρωμα διατροφής και δεν υποκαθιστά μια ισορροπημένη διατροφή και έναν υγιεινό τρόπο ζωής. Οι ισχυρισμοί βασίζονται σε εγκεκριμένους ισχυρισμούς υγείας της EFSA για τα περιεχόμενα συστατικά.",
    },
    "magnesium": {
        "name": "B2H Magnesium Ultra Complex",
        "label_url": "https://wearenextgen.github.io/b2h-viewer/assets/labels/magnesium.png",
        "usage_images": ["", "", "", ""],
        "tagline": "Η καθημερινή ισορροπία που χρειάζεται το σώμα και το μυαλό σας.",
        "benefit_intro": "Το μαγνήσιο συμμετέχει καθημερινά σε εκατοντάδες βιολογικές διεργασίες που επηρεάζουν την ενέργεια, τους μυς και το νευρικό σύστημα.",
        "micro_tagline": "Κάθε ημέρα λίγο περισσότερη ισορροπία.",
        "quality_intro": "Premium Magnesium Formula με υψηλή βιοδιαθεσιμότητα.",
        "palette": ("#d7c2ef", "#d6edf1", "#604c72", "#a77e4d"),
        "images": ["", "", "", "", "", ""],
        "image_cards": [
            ("Λιγότερη κόπωση", "Συμβάλλει στη μείωση της κόπωσης και της εξάντλησης."),
            ("Νευρικό σύστημα", "Υποστηρίζει τη φυσιολογική λειτουργία του νευρικού συστήματος."),
            ("Μυϊκή λειτουργία", "Συμβάλλει στη φυσιολογική λειτουργία των μυών."),
            ("Ενέργεια", "Υποστηρίζει τον φυσιολογικό ενεργειακό μεταβολισμό."),
            ("Βιοδιαθεσιμότητα", "Με Magnesium Bisglycinate υψηλής βιοδιαθεσιμότητας."),
            ("Ολοκληρωμένη σύνθεση", "Με ψευδάργυρο και βιταμίνη Β6."),
        ],
        "facts": [
            ("Κόπωση", "Το μαγνήσιο και η βιταμίνη Β6 συμβάλλουν στη μείωση της κόπωσης και της εξάντλησης."),
            ("Νευρικό σύστημα", "Υποστηρίζει τη φυσιολογική λειτουργία του νευρικού συστήματος."),
            ("Μύες", "Το μαγνήσιο συμβάλλει στη φυσιολογική λειτουργία των μυών."),
            ("Ενέργεια", "Υποστηρίζει τον φυσιολογικό ενεργειακό μεταβολισμό."),
        ],
        "benefits": [
            "Μείωση κόπωσης και εξάντλησης",
            "Φυσιολογική λειτουργία νευρικού συστήματος",
            "Φυσιολογική λειτουργία μυών",
            "Φυσιολογικός ενεργειακός μεταβολισμός",
            "Magnesium Bisglycinate υψηλής βιοδιαθεσιμότητας",
            "Ψευδάργυρος και βιταμίνη Β6",
        ],
        "benefit_icons": ["bolt", "brain", "muscle", "balance"],
        "benefit_tiles": [
            ("Λιγότερη κόπωση", "Υποστήριξη για τις απαιτήσεις της καθημερινότητας."),
            ("Νευρικό σύστημα", "Καθημερινή υποστήριξη της φυσιολογικής νευρικής λειτουργίας."),
            ("Μυϊκή λειτουργία", "Μαγνήσιο για τη φυσιολογική λειτουργία των μυών."),
            ("Ενεργειακός μεταβολισμός", "Σύνθεση που ακολουθεί τον ρυθμό της ζωής σας."),
        ],
        "why_intro": "Το B2H Magnesium Ultra Complex δημιουργήθηκε για όσους αναζητούν μια προηγμένη και αξιόπιστη καθημερινή λύση βασισμένη σε μορφή μαγνησίου υψηλής βιοδιαθεσιμότητας.",
        "why_detail": "Η σύνθεσή του συνδυάζει Magnesium Bisglycinate, ψευδάργυρο και βιταμίνη Β6, προσφέροντας ολοκληρωμένη μικροθρεπτική υποστήριξη ως μέρος ενός ισορροπημένου τρόπου ζωής.",
        "why_paragraphs": [
            "Το μαγνήσιο είναι ένα από τα σημαντικότερα μέταλλα για τη φυσιολογική λειτουργία του οργανισμού. Κάθε ημέρα συμμετέχει σε εκατοντάδες βιολογικές διεργασίες που επηρεάζουν την ενέργεια, τους μυς και το νευρικό σύστημα.",
            "Το B2H Magnesium Ultra Complex συνδυάζει υψηλής βιοδιαθεσιμότητας Magnesium Bisglycinate, ψευδάργυρο και βιταμίνη Β6, προσφέροντας μια ολοκληρωμένη καθημερινή υποστήριξη για όσους επιθυμούν να διατηρούν τον οργανισμό τους σε ισορροπία.",
            "Η προηγμένη του σύνθεση σχεδιάστηκε για να αποτελεί τον καθημερινό σύμμαχο του σύγχρονου ανθρώπου, υποστηρίζοντας τη φυσιολογική λειτουργία των μυών, του νευρικού συστήματος και του ενεργειακού μεταβολισμού.",
            "Οι απαιτήσεις της καθημερινότητας μπορούν να αυξήσουν τις ανάγκες του οργανισμού σε μαγνήσιο.",
            "Το B2H Magnesium Ultra Complex δημιουργήθηκε για όσους αναζητούν μια προηγμένη και αξιόπιστη καθημερινή λύση, βασισμένη σε μορφή μαγνησίου υψηλής βιοδιαθεσιμότητας.",
            "Η σύνθεσή του συνδυάζει Magnesium Bisglycinate, Ψευδάργυρο και Βιταμίνη Β6, προσφέροντας ολοκληρωμένη μικροθρεπτική υποστήριξη ως μέρος ενός ισορροπημένου τρόπου ζωής.",
        ],
        "ingredients": [
            ("Magnesium Bisglycinate", "Μορφή μαγνησίου υψηλής βιοδιαθεσιμότητας."),
            ("Ψευδάργυρος", "Συμπληρώνει την καθημερινή μικροθρεπτική υποστήριξη."),
            ("Βιταμίνη Β6", "Συμβάλλει στη μείωση της κόπωσης και στη φυσιολογική λειτουργία του νευρικού συστήματος."),
            ("Clinical Formula", "Premium πρώτες ύλες σε ολοκληρωμένη καθημερινή σύνθεση."),
        ],
        "quality": [
            ("Υψηλή βιοδιαθεσιμότητα", "Magnesium Bisglycinate για προηγμένη καθημερινή υποστήριξη."),
            ("Τριπλή σύνθεση", "Μαγνήσιο, ψευδάργυρος και βιταμίνη Β6."),
            ("Premium πρώτες ύλες", "Σταθερή ποιότητα για καθημερινή χρήση."),
            ("30 ταμπλέτες", "Πρακτική μορφή για σταθερή καθημερινή ρουτίνα."),
        ],
        "ideal_for": [
            "Άτομα με έντονους καθημερινούς ρυθμούς",
            "Εργαζόμενους με αυξημένες απαιτήσεις",
            "Αθλητικά δραστήριους ανθρώπους",
            "Άτομα που επιθυμούν καθημερινή υποστήριξη μυϊκής και νευρικής λειτουργίας",
            "Γυναίκες και άνδρες που αναζητούν ολοκληρωμένη στρατηγική ευζωίας",
        ],
        "stats": [("30", "Ταμπλέτες"), ("High", "Βιοδιαθεσιμότητα"), ("Daily", "Καθημερινή χρήση"), ("Premium", "Clinical Formula")],
        "usage": "Λαμβάνετε την προτεινόμενη ημερήσια δόση σύμφωνα με τις οδηγίες της συσκευασίας, κατά προτίμηση μετά από γεύμα.",
        "usage_steps": [
            ("01", "Ελέγξτε τη δόση", "Ακολουθήστε την προτεινόμενη ημερήσια δόση της τελικής συσκευασίας."),
            ("02", "Μετά από γεύμα", "Προτιμήστε τη λήψη μετά από γεύμα."),
            ("03", "Καθημερινή συνέπεια", "Η σταθερή χρήση υποστηρίζει τη μικροθρεπτική επάρκεια."),
        ],
        "usage_stat": ("30", "Ταμπλέτες"),
        "closing": ["Λιγότερη κόπωση. Περισσότερη ισορροπία. Κάθε ημέρα.", "Γιατί η καθημερινή ευζωία ξεκινά από τη σωστή υποστήριξη του οργανισμού."],
        "disclaimer": "Το μαγνήσιο συμβάλλει στη μείωση της κόπωσης και της εξάντλησης, στη φυσιολογική λειτουργία του νευρικού συστήματος, στη φυσιολογική λειτουργία των μυών και στον φυσιολογικό ενεργειακό μεταβολισμό. Η βιταμίνη Β6 συμβάλλει επίσης στη μείωση της κόπωσης και στη φυσιολογική λειτουργία του νευρικού συστήματος. Οι ισχυρισμοί βασίζονται αποκλειστικά στους εγκεκριμένους ισχυρισμούς υγείας της EFSA. Το προϊόν είναι συμπλήρωμα διατροφής και δεν υποκαθιστά μια ισορροπημένη διατροφή και έναν υγιεινό τρόπο ζωής.",
    },
}


ICONS = {
    "heart": '<path d="M32 55S8 41 8 23C8 8 27 4 32 17 37 4 56 8 56 23 56 41 32 55 32 55Z"/>',
    "brain": '<path d="M25 10c-8 0-12 7-10 13-8 5-5 17 3 19-1 8 9 13 15 7V15c0-3-3-5-8-5Zm14 0c8 0 12 7 10 13 8 5 5 17-3 19 1 8-9 13-15 7V15c0-3 3-5 8-5Z"/><path d="M19 26c7 0 8 5 8 9M45 26c-7 0-8 5-8 9"/>',
    "eye": '<path d="M5 32s10-16 27-16 27 16 27 16-10 16-27 16S5 32 5 32Z"/><circle cx="32" cy="32" r="8"/>',
    "fish": '<path d="M7 32c12-14 27-16 40-5l10-8v26l-10-8C34 48 19 46 7 32Z"/><circle cx="21" cy="29" r="2"/>',
    "bolt": '<path d="M36 5 15 35h15l-3 24 22-33H34l2-21Z"/>',
    "shield": '<path d="M32 5 54 14v16c0 15-9 24-22 29C19 54 10 45 10 30V14l22-9Z"/><path d="m22 31 7 7 14-16"/>',
    "cell": '<circle cx="32" cy="32" r="24"/><circle cx="32" cy="32" r="10"/><path d="M13 21c8 3 12-5 19-5M45 47c-7-3-10 2-17 1"/>',
    "bone": '<path d="M15 22c-7-1-9-10-3-14 5-3 9 1 10 5l20 29c4-1 8 2 8 7 0 7-9 10-13 4-3 2-8 0-9-4L9 28c-4 1-8-2-8-7 0-7 9-10 14-4Z"/>',
    "muscle": '<path d="M16 38c8-3 12-11 13-21l8 4-2 10c6-4 12-3 17 1 6 6 5 17-4 22-13 7-32 1-38-8l6-8Z"/>',
    "balance": '<path d="M32 8v45M17 14h30M11 49h42M17 14 8 33h18L17 14Zm30 0-9 19h18L47 14Z"/>',
}


def svg(name):
    body = ICONS.get(name, ICONS["shield"])
    return f'<svg viewBox="0 0 64 64" aria-hidden="true">{body}</svg>'


def html_list(items, tag="li"):
    return "".join(f"<{tag}>{escape(item)}</{tag}>" for item in items)


def common_tokens(product, root_id):
    gold, blue, brown, caramel = product["palette"]
    return f"""
<style>
#{root_id}{{--gold:{gold};--blue:{blue};--brown:{brown};--caramel:{caramel};--ink:#171513;--white:#fff;--edge:clamp(14px,3vw,42px);--max:1650px;box-sizing:border-box;width:100vw;margin-left:calc(50% - 50vw);font-family:Inter,-apple-system,BlinkMacSystemFont,\"Segoe UI\",sans-serif;color:var(--ink);background:#fff;position:relative;isolation:isolate}}
#{root_id},#{root_id} *{{box-sizing:border-box}}
#{root_id} button{{font:inherit}}
#{root_id} .sr-only{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}}
#{root_id} .shell{{width:min(calc(100% - (var(--edge)*2)),var(--max));margin:auto}}
#{root_id} .soft{{background:linear-gradient(135deg,color-mix(in srgb,var(--gold) 78%,white),color-mix(in srgb,var(--blue) 82%,white));box-shadow:0 22px 60px rgba(117,92,73,.13)}}
#{root_id} .checker:nth-child(4n+1),#{root_id} .checker:nth-child(4n+4){{background:linear-gradient(145deg,var(--brown),color-mix(in srgb,var(--brown) 72%,var(--caramel)));color:white}}
#{root_id} .checker:nth-child(4n+2),#{root_id} .checker:nth-child(4n+3){{background:linear-gradient(145deg,color-mix(in srgb,var(--blue) 82%,white),color-mix(in srgb,var(--gold) 76%,white));color:var(--brown)}}
#{root_id} svg{{width:1.8em;height:1.8em;fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}}
#{root_id} .eyebrow{{font-size:.76rem;letter-spacing:.15em;text-transform:uppercase;font-weight:800;color:var(--caramel)}}
#{root_id} h3,#{root_id} p{{margin-top:0}}
@media(max-width:720px){{#{root_id}{{--edge:14px}}}}
</style>"""


def render_benefits(slug, product):
    root = f"b2h-{slug}-benefits"
    cards = "".join(
        f'<figure class="photo-card" data-index="{index}"><div class="photo-media"><span class="slot">IMAGE {index + 1}</span></div><figcaption><strong>{escape(title)}</strong><p>{escape(text)}</p></figcaption></figure>'
        for index, (title, text) in enumerate(product["image_cards"])
    )
    fact_buttons = "".join(
        f'<button type="button" class="fact{" is-active" if index == 0 else ""}" data-title="{escape(title)}" data-copy="{escape(text)}" aria-pressed="{"true" if index == 0 else "false"}">{escape(title)}</button>'
        for index, (title, text) in enumerate(product["facts"])
    )
    tiles = "".join(
        f'<article class="benefit checker"><span>{svg(product["benefit_icons"][index])}</span><h3>{escape(title)}</h3><p>{escape(text)}</p></article>'
        for index, (title, text) in enumerate(product["benefit_tiles"])
    )
    urls = ",\n    ".join(repr(url) for url in product["images"])
    first_title, first_copy = product["facts"][0]
    return f"""<!-- B2H {escape(product['name'])} / SECTION 01: BENEFITS -->
<section id="{root}" aria-label="{escape(product['name'])} benefits">
  <h2 class="sr-only">{escape(product['name'])} - Οφέλη</h2>
  <div class="shell">
    <div class="photo-grid">{cards}</div>
    <div class="facts soft">
      <div class="intro"><span class="eyebrow">B2H Clinical Series · {escape(product['name'])}</span><p>{escape(product['tagline'])}</p><small>{escape(product['benefit_intro'])}</small><b>{escape(product['micro_tagline'])}</b><em>Επιλέξτε μια κάρτα για περισσότερες πληροφορίες.</em></div>
      <div class="fact-buttons">{fact_buttons}</div>
      <article class="fact-panel"><span class="eyebrow">Επιλεγμένη πληροφορία</span><h3>{escape(first_title)}</h3><p>{escape(first_copy)}</p><ul>{html_list(product['benefits'])}</ul></article>
    </div>
    <div class="benefit-grid">{tiles}</div>
  </div>
</section>
{common_tokens(product, root)}
<style>
#{root}{{padding:clamp(24px,4vw,58px) 0}}
#{root} .photo-grid{{display:grid;grid-template-columns:1.35fr .82fr 1fr;grid-template-rows:repeat(2,clamp(210px,22vw,380px));gap:clamp(12px,1.6vw,24px);margin-bottom:clamp(24px,4vw,52px)}}
#{root} .photo-card{{margin:0;position:relative;border-radius:clamp(18px,2vw,30px);overflow:hidden;cursor:grab;touch-action:none;box-shadow:0 18px 44px rgba(71,53,41,.16);transform:translate3d(0,0,0);transition:transform .45s cubic-bezier(.22,1,.36,1),box-shadow .3s}}
#{root} .photo-card:active{{cursor:grabbing}}
#{root} .photo-media{{width:100%;height:100%;background:linear-gradient(135deg,var(--gold),var(--blue));background-size:cover;background-position:center;transition:filter .35s,transform .45s}}
#{root} .photo-card:nth-child(2n) .photo-media{{background-image:linear-gradient(145deg,var(--blue),var(--gold))}}
#{root} .slot{{position:absolute;inset:0;display:grid;place-items:center;color:var(--brown);font-weight:900;letter-spacing:.15em;opacity:.55}}
#{root} figcaption{{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:flex-end;padding:clamp(18px,2vw,30px);background:linear-gradient(transparent 20%,rgba(20,18,17,.84));color:white;opacity:0;transform:translateY(12px);transition:.35s;pointer-events:none}}
#{root} figcaption strong{{font-size:clamp(1rem,1.5vw,1.45rem);text-transform:uppercase}}
#{root} figcaption p{{margin:.55rem 0 0;line-height:1.45;max-width:38ch}}
#{root} .photo-card.is-open figcaption{{opacity:1;transform:none}}
#{root} .photo-card.is-open .photo-media{{filter:blur(4px) brightness(.58);transform:scale(1.05)}}
#{root} .facts{{border-radius:clamp(24px,3vw,42px);padding:clamp(22px,4vw,54px);display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(20px,3vw,46px);margin-bottom:clamp(22px,3vw,42px)}}
#{root} .intro p{{font-size:clamp(1.6rem,3vw,3.2rem);font-weight:850;line-height:1.05;margin:.65rem 0 1rem;max-width:18ch}}
#{root} .intro small{{display:block;color:var(--brown);line-height:1.55;font-size:.96rem}}
#{root} .intro b{{display:block;margin-top:.7rem;color:var(--brown);font-size:.9rem}}
#{root} .intro em{{display:block;margin-top:.8rem;color:var(--caramel);font-size:.78rem;font-style:normal;font-weight:800}}
#{root} .fact-buttons{{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;align-self:start}}
#{root} .fact{{border:0;border-radius:18px;padding:18px 14px;background:rgba(255,255,255,.72);color:var(--brown);font-weight:800;cursor:pointer;box-shadow:0 10px 26px rgba(117,92,73,.08);transition:transform .2s,background .2s,color .2s}}
#{root} .fact:hover{{transform:translateY(-3px)}}
#{root} .fact.is-active{{background:var(--brown);color:white}}
#{root} .fact-panel{{grid-column:1/-1;background:rgba(255,255,255,.78);border-radius:24px;padding:clamp(20px,3vw,34px);min-height:270px}}
#{root} .fact-panel h3{{font-size:clamp(1.5rem,2.4vw,2.45rem);margin:.5rem 0}}
#{root} .fact-panel p{{font-size:clamp(1rem,1.3vw,1.2rem);line-height:1.65}}
#{root} .fact-panel ul{{columns:2;gap:32px;padding-left:1.2rem;margin:1.2rem 0 0}}
#{root} .fact-panel li{{margin:.55rem 0;break-inside:avoid}}
#{root} .benefit-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:clamp(14px,2vw,24px)}}
#{root} .benefit{{min-height:220px;border-radius:clamp(22px,2.5vw,36px);padding:clamp(24px,3vw,40px);display:flex;flex-direction:column;justify-content:center;box-shadow:0 16px 40px rgba(69,52,40,.12);transition:transform .3s}}
#{root} .benefit:hover{{transform:translateY(-5px)}}
#{root} .benefit span{{font-size:1.45rem}}
#{root} .benefit h3{{margin:1rem 0 .55rem;font-size:clamp(1.05rem,1.5vw,1.35rem);text-transform:uppercase}}
#{root} .benefit p{{margin:0;line-height:1.55;opacity:.84}}
@media(max-width:720px){{#{root} .photo-grid{{grid-template-rows:repeat(2,clamp(150px,43vw,230px));gap:9px}}#{root} .photo-card{{border-radius:15px}}#{root} figcaption{{padding:12px}}#{root} figcaption p{{font-size:.76rem}}#{root} .facts{{grid-template-columns:1fr}}#{root} .fact-panel{{grid-column:auto}}#{root} .fact-panel ul{{columns:1}}#{root} .benefit-grid{{grid-template-columns:1fr 1fr}}#{root} .benefit{{min-height:190px;padding:20px}}}}
</style>
<script>
(() => {{
  const root = document.getElementById('{root}');
  if (!root || root.dataset.ready) return;
  root.dataset.ready = 'true';
  const IMAGE_URLS = [
    {urls}
  ]; // Replace empty strings with public image URLs.
  root.querySelectorAll('.photo-card').forEach((card, index) => {{
    const media = card.querySelector('.photo-media');
    const slot = card.querySelector('.slot');
    if (IMAGE_URLS[index]) {{ media.style.backgroundImage = `url("${{IMAGE_URLS[index]}}")`; slot.hidden = true; }}
    let startX = 0, startY = 0, dx = 0, dy = 0, moved = false;
    card.addEventListener('pointerdown', event => {{ startX = event.clientX; startY = event.clientY; moved = false; card.setPointerCapture(event.pointerId); card.style.transition = 'none'; }});
    card.addEventListener('pointermove', event => {{ if (!card.hasPointerCapture(event.pointerId)) return; const bounds = root.getBoundingClientRect(); const cardBounds = card.getBoundingClientRect(); dx = Math.max(bounds.left - cardBounds.left + dx, Math.min(bounds.right - cardBounds.right + dx, event.clientX - startX)); dy = Math.max(-cardBounds.top + 12 + dy, Math.min(window.innerHeight - cardBounds.bottom + dy, event.clientY - startY)); moved = Math.abs(dx) + Math.abs(dy) > 8; card.style.transform = `translate3d(${{dx}}px,${{dy}}px,0)`; }});
    card.addEventListener('pointerup', event => {{ card.releasePointerCapture(event.pointerId); card.style.transition = ''; card.style.transform = 'translate3d(0,0,0)'; dx = 0; dy = 0; if (!moved) card.classList.toggle('is-open'); }});
    card.addEventListener('pointercancel', () => {{ card.style.transition = ''; card.style.transform = 'translate3d(0,0,0)'; dx = 0; dy = 0; }});
  }});
  const title = root.querySelector('.fact-panel h3');
  const copy = root.querySelector('.fact-panel p');
  root.querySelectorAll('.fact').forEach(button => button.addEventListener('click', () => {{ root.querySelectorAll('.fact').forEach(item => {{ item.classList.remove('is-active'); item.setAttribute('aria-pressed','false'); }}); button.classList.add('is-active'); button.setAttribute('aria-pressed','true'); title.textContent = button.dataset.title; copy.textContent = button.dataset.copy; }}));
}})();
</script>
"""


def render_why(slug, product):
    root = f"b2h-{slug}-why"
    buttons = "".join(f'<button class="ingredient{" is-active" if i == 0 else ""}" type="button" data-title="{escape(a)}" data-copy="{escape(b)}">{escape(a)}</button>' for i, (a, b) in enumerate(product["ingredients"]))
    first = product["ingredients"][0]
    narrative = "".join(f"<p>{escape(paragraph)}</p>" for paragraph in product["why_paragraphs"])
    return f"""<!-- B2H {escape(product['name'])} / SECTION 02: WHY CHOOSE -->
<section id="{root}" aria-label="Why choose {escape(product['name'])}">
  <h2 class="sr-only">Γιατί να επιλέξετε το {escape(product['name'])}</h2>
  <div class="shell layout">
    <div class="formula-stage soft" aria-hidden="true">
      <div class="formula-orbit formula-orbit--one"></div>
      <div class="formula-orbit formula-orbit--two"></div>
      <div class="formula-core">{svg(product['benefit_icons'][0])}<strong>CLINICAL<br>FORMULA</strong></div>
      <span class="formula-chip formula-chip--one">01</span>
      <span class="formula-chip formula-chip--two">02</span>
      <span class="formula-chip formula-chip--three">03</span>
      <span class="formula-chip formula-chip--four">04</span>
    </div>
    <article class="story">
      <span class="eyebrow">B2H Clinical Series · {escape(product['name'])}</span>
      <p class="lead">{escape(product['why_intro'])}</p>
      <details class="approved-copy"><summary>Πλήρης εγκεκριμένη πληροφορία</summary><div>{narrative}</div></details>
      <div class="ingredient-buttons">{buttons}</div>
      <div class="ingredient-panel"><strong>{escape(first[0])}</strong><p>{escape(first[1])}</p></div>
    </article>
  </div>
</section>
{common_tokens(product, root)}
<style>
#{root}{{padding:clamp(26px,5vw,76px) 0}}
#{root} .layout{{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(320px,.95fr);gap:clamp(18px,3vw,46px);align-items:stretch}}
#{root} .formula-stage{{position:relative;min-height:clamp(520px,58vw,760px);border-radius:clamp(26px,3vw,44px);overflow:hidden;display:grid;place-items:center}}
#{root} .formula-stage:before{{content:"";position:absolute;inset:9%;border-radius:42% 58% 52% 48%;background:radial-gradient(circle at 35% 25%,rgba(255,255,255,.96),rgba(255,255,255,.18) 58%,transparent 60%);filter:blur(1px)}}
#{root} .formula-orbit{{position:absolute;border:1px solid color-mix(in srgb,var(--brown) 24%,transparent);border-radius:50%;animation:b2hOrbit 18s linear infinite}}
#{root} .formula-orbit--one{{width:68%;aspect-ratio:1;transform:rotate(18deg)}}
#{root} .formula-orbit--two{{width:48%;aspect-ratio:1;transform:rotate(-24deg);animation-direction:reverse;animation-duration:13s}}
#{root} .formula-core{{position:relative;z-index:2;width:clamp(190px,26vw,330px);aspect-ratio:1;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;text-align:center;background:linear-gradient(145deg,var(--brown),color-mix(in srgb,var(--brown) 68%,var(--caramel)));color:#fff;box-shadow:0 28px 65px rgba(70,50,38,.25)}}
#{root} .formula-core svg{{font-size:2rem}}
#{root} .formula-core strong{{font-size:clamp(1.25rem,2.3vw,2rem);letter-spacing:.08em;line-height:1}}
#{root} .formula-chip{{position:absolute;z-index:3;width:58px;height:58px;border-radius:18px;display:grid;place-items:center;background:#fff;color:var(--brown);font-weight:900;box-shadow:0 12px 30px rgba(70,50,38,.15)}}
#{root} .formula-chip--one{{top:14%;left:18%}}#{root} .formula-chip--two{{top:22%;right:13%}}#{root} .formula-chip--three{{bottom:17%;left:12%}}#{root} .formula-chip--four{{right:20%;bottom:11%}}
@keyframes b2hOrbit{{to{{rotate:360deg}}}}
#{root} .story{{border-radius:clamp(26px,3vw,44px);padding:clamp(26px,4vw,58px);background:linear-gradient(160deg,#fff,color-mix(in srgb,var(--blue) 45%,white));box-shadow:0 22px 60px rgba(117,92,73,.12)}}
#{root} .lead{{font-size:clamp(1.5rem,2.7vw,2.9rem);line-height:1.08;font-weight:850;margin:.7rem 0 1.3rem}}
#{root} .story>p:not(.lead){{line-height:1.7;font-size:1.05rem;color:var(--brown)}}
#{root} .approved-copy{{margin:1.4rem 0;color:var(--brown)}}
#{root} .approved-copy summary{{cursor:pointer;font-weight:850;color:var(--caramel);padding:.7rem 0}}
#{root} .approved-copy div{{max-height:290px;overflow:auto;padding:4px 14px 4px 0;scrollbar-color:var(--caramel) transparent}}
#{root} .approved-copy p{{line-height:1.65;margin:.75rem 0}}
#{root} .ingredient-buttons{{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:2rem 0 14px}}
#{root} .ingredient{{border:0;border-radius:16px;padding:16px;background:color-mix(in srgb,var(--gold) 62%,white);color:var(--brown);font-weight:800;cursor:pointer;transition:.25s}}
#{root} .ingredient:hover{{transform:translateY(-3px)}}
#{root} .ingredient.is-active{{background:var(--brown);color:white}}
#{root} .ingredient-panel{{min-height:145px;border-radius:20px;padding:24px;background:linear-gradient(145deg,var(--brown),color-mix(in srgb,var(--brown) 72%,var(--caramel)));color:white}}
#{root} .ingredient-panel strong{{font-size:1.25rem}}
#{root} .ingredient-panel p{{margin:.65rem 0 0;line-height:1.55;opacity:.88}}
@media(max-width:900px){{#{root} .layout{{grid-template-columns:1fr}}#{root} .formula-stage{{min-height:560px}}}}
@media(max-width:560px){{#{root} .formula-stage{{min-height:430px}}#{root} .ingredient-buttons{{grid-template-columns:1fr 1fr}}}}
</style>
<script>
(() => {{
  const root = document.getElementById('{root}');
  if (!root || root.dataset.ready) return; root.dataset.ready='true';
  const panelTitle=root.querySelector('.ingredient-panel strong'), panelCopy=root.querySelector('.ingredient-panel p');
  root.querySelectorAll('.ingredient').forEach(button=>button.addEventListener('click',()=>{{root.querySelectorAll('.ingredient').forEach(item=>item.classList.remove('is-active'));button.classList.add('is-active');panelTitle.textContent=button.dataset.title;panelCopy.textContent=button.dataset.copy;}}));
}})();
</script>
"""


def render_quality(slug, product):
    root = f"b2h-{slug}-quality"
    cards = "".join(f'<article class="quality checker"><span>{svg(["shield","cell","balance","bolt"][i])}</span><h3>{escape(a)}</h3><p>{escape(b)}</p></article>' for i, (a, b) in enumerate(product["quality"]))
    audience = "".join(f'<button type="button" class="audience{" is-active" if i == 0 else ""}" data-copy="{escape(item)}">{escape(item)}</button>' for i, item in enumerate(product["ideal_for"]))
    stats = "".join(f'<div class="stat"><strong>{escape(value)}</strong><span>{escape(label)}</span></div>' for value, label in product["stats"])
    return f"""<!-- B2H {escape(product['name'])} / SECTION 03: QUALITY & FORMULA -->
<section id="{root}" aria-label="{escape(product['name'])} quality and formulation">
  <h2 class="sr-only">{escape(product['name'])} - Σύνθεση και ποιότητα</h2>
  <div class="shell">
    <p class="quality-intro"><span class="eyebrow">B2H Clinical Series</span>{escape(product['quality_intro'])}</p>
    <div class="quality-grid">{cards}</div>
    <div class="stats">{stats}</div>
    <div class="audience-wrap soft">
      <div><span class="eyebrow">Ιδανικό για</span><p class="audience-copy">{escape(product['ideal_for'][0])}</p></div>
      <div class="audience-buttons">{audience}</div>
    </div>
    <div class="image-band"><span>OPTIONAL FORMULA / PACKAGING IMAGE</span></div>
  </div>
</section>
{common_tokens(product, root)}
<style>
#{root}{{padding:clamp(26px,5vw,76px) 0}}
#{root} .quality-intro{{display:flex;flex-direction:column;gap:.6rem;margin:0 0 clamp(18px,3vw,34px);font-size:clamp(1.35rem,2.5vw,2.45rem);font-weight:850;color:var(--brown);max-width:28ch;line-height:1.1}}
#{root} .quality-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:clamp(14px,2vw,24px)}}
#{root} .quality{{border-radius:clamp(22px,3vw,40px);min-height:270px;padding:clamp(25px,4vw,48px);display:flex;flex-direction:column;justify-content:center;box-shadow:0 18px 44px rgba(77,59,46,.12);transition:transform .3s}}
#{root} .quality:hover{{transform:translateY(-6px)}}
#{root} .quality span{{font-size:1.6rem}}
#{root} .quality h3{{font-size:clamp(1.2rem,2vw,1.85rem);margin:1rem 0 .6rem;text-transform:uppercase}}
#{root} .quality p{{line-height:1.6;margin:0;max-width:48ch;opacity:.85}}
#{root} .stats{{display:grid;grid-template-columns:repeat({len(product['stats'])},1fr);gap:12px;margin-top:clamp(18px,3vw,34px)}}
#{root} .stat{{min-height:120px;border-radius:20px;padding:20px;display:flex;flex-direction:column;justify-content:center;text-align:center;background:linear-gradient(145deg,color-mix(in srgb,var(--gold) 72%,white),color-mix(in srgb,var(--blue) 70%,white));color:var(--brown)}}
#{root} .stat strong{{font-size:clamp(1.5rem,3vw,2.7rem);line-height:1}}
#{root} .stat span{{margin-top:.55rem;font-size:.78rem;font-weight:800;text-transform:uppercase}}
#{root} .audience-wrap{{margin-top:clamp(18px,3vw,34px);border-radius:clamp(22px,3vw,40px);padding:clamp(24px,4vw,48px);display:grid;grid-template-columns:.8fr 1.2fr;gap:30px;align-items:center}}
#{root} .audience-copy{{font-size:clamp(1.5rem,2.8vw,2.8rem);font-weight:850;line-height:1.08;margin:.7rem 0 0}}
#{root} .audience-buttons{{display:flex;flex-wrap:wrap;gap:10px}}
#{root} .audience{{border:0;border-radius:999px;padding:13px 17px;background:rgba(255,255,255,.75);color:var(--brown);font-weight:750;cursor:pointer;transition:.2s}}
#{root} .audience:hover{{transform:translateY(-2px)}}
#{root} .audience.is-active{{background:var(--brown);color:white}}
#{root} .image-band{{margin-top:clamp(18px,3vw,34px);height:clamp(260px,35vw,500px);border-radius:clamp(22px,3vw,40px);display:grid;place-items:center;background:linear-gradient(125deg,var(--blue),var(--gold));background-size:cover;background-position:center;color:var(--brown);font-weight:900;letter-spacing:.12em;text-align:center;overflow:hidden}}
@media(max-width:720px){{#{root} .quality-grid{{grid-template-columns:1fr 1fr}}#{root} .quality{{min-height:230px;padding:20px}}#{root} .stats{{grid-template-columns:repeat(2,1fr)}}#{root} .audience-wrap{{grid-template-columns:1fr}}}}
</style>
<script>
(() => {{
  const root=document.getElementById('{root}');if(!root||root.dataset.ready)return;root.dataset.ready='true';
  const IMAGE_URL=''; // Optional public formula/packaging image URL.
  const band=root.querySelector('.image-band');if(IMAGE_URL){{band.style.backgroundImage=`linear-gradient(rgba(20,18,17,.08),rgba(20,18,17,.35)),url("${{IMAGE_URL}}")`;band.querySelector('span').hidden=true;}}
  const copy=root.querySelector('.audience-copy');root.querySelectorAll('.audience').forEach(button=>button.addEventListener('click',()=>{{root.querySelectorAll('.audience').forEach(item=>item.classList.remove('is-active'));button.classList.add('is-active');copy.textContent=button.dataset.copy;}}));
}})();
</script>
"""


def render_usage(slug, product):
    root = f"b2h-{slug}-usage"
    steps = "".join(f'<button type="button" class="step checker{" is-active" if i == 0 else ""}" data-title="{escape(title)}" data-copy="{escape(copy)}"><span>{num}</span><strong>{escape(title)}</strong></button>' for i, (num, title, copy) in enumerate(product["usage_steps"]))
    first = product["usage_steps"][0]
    closing = "".join(f"<p>{escape(line)}</p>" for line in product["closing"])
    image_urls = ",\n    ".join(repr(url) for url in product["usage_images"])
    return f"""<!-- B2H {escape(product['name'])} / SECTION 04: HOW TO USE -->
<section id="{root}" aria-label="How to use {escape(product['name'])}">
  <h2 class="sr-only">{escape(product['name'])} - Οδηγίες χρήσης</h2>
  <div class="shell usage-wrap soft">
    <div class="usage-top">
      <div class="usage-main">
        <span class="eyebrow">{escape(product['name'])}</span>
        <p class="lead">{escape(product['usage'])}</p>
        <div class="steps">{steps}</div>
        <article class="step-panel"><strong>{escape(first[1])}</strong><p>{escape(first[2])}</p></article>
      </div>
      <aside class="dose-card">
        <span class="dose-number">{escape(product['usage_stat'][0])}</span>
        <strong>{escape(product['usage_stat'][1])}</strong>
        <small>Σταθερή καθημερινή ρουτίνα</small>
      </aside>
    </div>
    <div class="model-collage">
      <div class="photo-stack photo-stack--left">
        <div class="usage-photo" data-index="0"><span>IMAGE 1</span></div>
        <div class="usage-photo" data-index="1"><span>IMAGE 2</span></div>
      </div>
      <div class="bottle-stage" aria-label="Interactive 3D bottle for {escape(product['name'])}">
        <canvas class="bottle-canvas"></canvas>
        <div class="model-status"><strong>3D PRODUCT</strong><span>Loading interactive bottle…</span></div>
        <p class="model-hint">Σύρετε για περιστροφή · Scroll για zoom</p>
      </div>
      <div class="photo-stack photo-stack--right">
        <div class="usage-photo" data-index="2"><span>IMAGE 3</span></div>
        <div class="usage-photo" data-index="3"><span>IMAGE 4</span></div>
      </div>
    </div>
    <div class="closing-copy">{closing}</div>
    <p class="disclaimer">{escape(product['disclaimer'])}</p>
  </div>
</section>
{common_tokens(product, root)}
<style>
#{root}{{padding:clamp(26px,5vw,76px) 0}}
#{root} .usage-wrap{{border-radius:clamp(26px,3vw,46px);padding:clamp(24px,4vw,56px)}}
#{root} .usage-top{{display:grid;grid-template-columns:1.2fr .8fr;gap:clamp(20px,4vw,54px)}}
#{root} .lead{{font-size:clamp(1.4rem,2.5vw,2.55rem);font-weight:850;line-height:1.12;margin:.7rem 0 1.8rem;max-width:25ch}}
#{root} .steps{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}}
#{root} .step{{border:0;border-radius:20px;min-height:150px;padding:20px;text-align:left;display:flex;flex-direction:column;justify-content:space-between;cursor:pointer;transition:transform .25s}}
#{root} .step:hover{{transform:translateY(-4px)}}
#{root} .step span{{font-size:1.8rem;font-weight:900;opacity:.45}}
#{root} .step strong{{font-size:1rem;text-transform:uppercase}}
#{root} .step.is-active{{outline:3px solid var(--caramel);outline-offset:3px}}
#{root} .step-panel{{margin-top:16px;min-height:130px;border-radius:20px;padding:24px;background:rgba(255,255,255,.8)}}
#{root} .step-panel strong{{font-size:1.25rem}}
#{root} .step-panel p{{margin:.6rem 0 0;line-height:1.6;color:var(--brown)}}
#{root} .dose-card{{border-radius:clamp(24px,3vw,38px);padding:clamp(24px,4vw,46px);background:linear-gradient(145deg,var(--brown),color-mix(in srgb,var(--brown) 70%,var(--caramel)));color:white;display:flex;flex-direction:column;justify-content:center;text-align:center;overflow:hidden;min-height:430px}}
#{root} .dose-number{{font-size:clamp(5rem,10vw,10rem);font-weight:950;line-height:.8}}
#{root} .dose-card>strong{{font-size:clamp(1rem,1.8vw,1.45rem);text-transform:uppercase;margin:1rem 0 2rem}}
#{root} .dose-card small{{opacity:.72;font-weight:700}}
#{root} .model-collage{{display:grid;grid-template-columns:minmax(150px,.42fr) minmax(360px,1.16fr) minmax(150px,.42fr);gap:clamp(12px,2vw,24px);margin-top:clamp(22px,4vw,48px);align-items:stretch}}
#{root} .photo-stack{{display:grid;grid-template-rows:1fr 1fr;gap:clamp(12px,2vw,24px)}}
#{root} .usage-photo{{min-height:210px;border-radius:clamp(20px,2.5vw,34px);display:grid;place-items:center;background:linear-gradient(145deg,var(--gold),var(--blue));background-size:cover;background-position:center;overflow:hidden;box-shadow:0 16px 40px rgba(77,59,46,.12);transition:transform .3s}}
#{root} .usage-photo:nth-child(2){{background-image:linear-gradient(145deg,var(--blue),var(--gold))}}
#{root} .usage-photo:hover{{transform:translateY(-5px)}}
#{root} .usage-photo span{{font-size:.72rem;font-weight:900;letter-spacing:.13em;color:var(--brown);opacity:.58}}
#{root} .bottle-stage{{position:relative;min-height:clamp(560px,58vw,760px);border-radius:clamp(24px,3vw,42px);overflow:hidden;background:radial-gradient(circle at 50% 35%,#fff 0 22%,color-mix(in srgb,var(--blue) 55%,white) 58%,color-mix(in srgb,var(--gold) 72%,white));box-shadow:inset 0 0 0 1px rgba(255,255,255,.65),0 24px 60px rgba(77,59,46,.16)}}
#{root} .bottle-canvas{{display:block;width:100%;height:100%;touch-action:pan-y;cursor:grab}}
#{root} .bottle-canvas:active{{cursor:grabbing}}
#{root} .model-status{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:.5rem;color:var(--brown);pointer-events:none;transition:opacity .35s}}
#{root} .model-status strong{{font-size:clamp(2.4rem,5vw,5rem);opacity:.13}}
#{root} .model-status span{{font-size:.78rem;font-weight:800;letter-spacing:.08em}}
#{root} .model-status.is-hidden{{opacity:0}}
#{root} .model-hint{{position:absolute;left:50%;bottom:18px;transform:translateX(-50%);margin:0;padding:9px 14px;border-radius:999px;background:rgba(255,255,255,.72);color:var(--brown);font-size:.72rem;font-weight:800;white-space:nowrap;backdrop-filter:blur(10px)}}
#{root} .closing-copy{{margin-top:clamp(22px,4vw,48px);text-align:center;padding:clamp(18px,3vw,34px);border-radius:22px;background:rgba(255,255,255,.58);color:var(--brown)}}
#{root} .closing-copy p{{margin:.35rem 0;font-size:clamp(1rem,1.7vw,1.35rem);font-weight:800}}
#{root} .disclaimer{{margin:20px 0 0;padding-top:20px;border-top:1px solid rgba(117,92,73,.22);font-size:.82rem;line-height:1.55;color:var(--brown)}}
@media(max-width:900px){{#{root} .usage-top{{grid-template-columns:1fr}}#{root} .dose-card{{min-height:300px}}#{root} .model-collage{{grid-template-columns:1fr 1fr}}#{root} .bottle-stage{{grid-column:1/-1;grid-row:1;min-height:600px}}#{root} .photo-stack{{grid-template-columns:1fr 1fr;grid-template-rows:1fr}}}}
@media(max-width:560px){{#{root} .steps{{grid-template-columns:1fr}}#{root} .step{{min-height:110px}}#{root} .model-collage{{grid-template-columns:1fr}}#{root} .bottle-stage{{min-height:500px}}#{root} .photo-stack{{grid-template-columns:1fr 1fr}}#{root} .usage-photo{{min-height:150px}}}}
</style>
<script>
(() => {{
  const root=document.getElementById('{root}');if(!root||root.dataset.ready)return;root.dataset.ready='true';
  const USAGE_IMAGE_URLS=[
    {image_urls}
  ]; // Replace empty strings with public rounded-card image URLs.
  root.querySelectorAll('.usage-photo').forEach((card,index)=>{{if(USAGE_IMAGE_URLS[index]){{card.style.backgroundImage=`url("${{USAGE_IMAGE_URLS[index]}}")`;card.querySelector('span').hidden=true;}}}});
  const title=root.querySelector('.step-panel strong'),copy=root.querySelector('.step-panel p');root.querySelectorAll('.step').forEach(button=>button.addEventListener('click',()=>{{root.querySelectorAll('.step').forEach(item=>item.classList.remove('is-active'));button.classList.add('is-active');title.textContent=button.dataset.title;copy.textContent=button.dataset.copy;}}));
}})();
</script>
<script type="module">
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.164.0/build/three.module.js';
import {{ OrbitControls }} from 'https://cdn.jsdelivr.net/npm/three@0.164.0/examples/jsm/controls/OrbitControls.js';
import {{ GLTFLoader }} from 'https://cdn.jsdelivr.net/npm/three@0.164.0/examples/jsm/loaders/GLTFLoader.js';

const root=document.getElementById('{root}');
if(root&&!root.dataset.modelReady){{
  root.dataset.modelReady='true';
  const MODEL_URL='https://wearenextgen.github.io/b2h-viewer/assets/models/b2h-bottle-base.glb';
  const LABEL_URL='{product['label_url']}';
  const canvas=root.querySelector('.bottle-canvas'),stage=root.querySelector('.bottle-stage'),status=root.querySelector('.model-status');
  const initialize=()=>{{
    const renderer=new THREE.WebGLRenderer({{canvas,antialias:true,alpha:true}});renderer.setPixelRatio(Math.min(devicePixelRatio,1.75));renderer.outputColorSpace=THREE.SRGBColorSpace;renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.08;
    const scene=new THREE.Scene();const camera=new THREE.PerspectiveCamera(34,1,.001,1000);
    const controls=new OrbitControls(camera,canvas);controls.enableDamping=true;controls.dampingFactor=.07;controls.autoRotate=true;controls.autoRotateSpeed=1.35;controls.enablePan=false;controls.minPolarAngle=Math.PI*.18;controls.maxPolarAngle=Math.PI*.78;canvas.addEventListener('pointerdown',()=>controls.autoRotate=false,{{once:true}});
    scene.add(new THREE.HemisphereLight(0xffffff,0xc9d9df,2.2));const key=new THREE.DirectionalLight(0xfff8ec,2.3);key.position.set(3,5,4);scene.add(key);const fill=new THREE.DirectionalLight(0xd7ecff,1.35);fill.position.set(-4,2,-3);scene.add(fill);const rim=new THREE.DirectionalLight(0xffffff,.8);rim.position.set(0,4,-5);scene.add(rim);
    const labelTexture=new THREE.TextureLoader().load(LABEL_URL);labelTexture.colorSpace=THREE.SRGBColorSpace;labelTexture.anisotropy=Math.min(16,renderer.capabilities.getMaxAnisotropy());
    new GLTFLoader().load(MODEL_URL,gltf=>{{
      const model=gltf.scene;const box=new THREE.Box3().setFromObject(model);const center=box.getCenter(new THREE.Vector3());model.position.sub(center);scene.add(model);
      const worldBox=new THREE.Box3().setFromObject(model),size=worldBox.getSize(new THREE.Vector3()),maxDim=Math.max(size.x,size.y,size.z);camera.position.set(0,size.y*.02,maxDim*1.92);controls.target.set(0,0,0);controls.minDistance=maxDim*.95;controls.maxDistance=maxDim*4;controls.update();
      const yMin=worldBox.min.y+size.y*.075,yMax=worldBox.min.y+size.y*.69,labelHeight=yMax-yMin,radius=Math.max(size.x,size.z)/2*1.016;const geometry=new THREE.CylinderGeometry(radius,radius,labelHeight,128,1,true);const material=new THREE.MeshStandardMaterial({{map:labelTexture,roughness:.3,metalness:0,side:THREE.FrontSide}});const label=new THREE.Mesh(geometry,material);label.position.y=(yMin+yMax)/2;label.rotation.y=Math.PI/2;scene.add(label);status.classList.add('is-hidden');
    }},xhr=>{{if(xhr.total)status.querySelector('span').textContent=`Loading 3D… ${{Math.round(xhr.loaded/xhr.total*100)}}%`;}},()=>{{status.querySelector('span').textContent='3D model unavailable';}});
    const resize=()=>{{const width=stage.clientWidth,height=stage.clientHeight;renderer.setSize(width,height,false);camera.aspect=width/height;camera.updateProjectionMatrix();}};new ResizeObserver(resize).observe(stage);resize();let active=true;const observer=new IntersectionObserver(entries=>active=entries[0].isIntersecting,{{rootMargin:'120px'}});observer.observe(stage);const animate=()=>{{requestAnimationFrame(animate);if(!active)return;controls.update();renderer.render(scene,camera);}};animate();
  }};
  const observer=new IntersectionObserver(entries=>{{if(entries[0].isIntersecting){{observer.disconnect();initialize();}}}},{{rootMargin:'300px'}});observer.observe(stage);
}}
</script>
"""


def build():
    for slug, product in PRODUCTS.items():
        target = OUTPUT / slug
        target.mkdir(parents=True, exist_ok=True)
        files = {
            "01-benefits.html": render_benefits(slug, product),
            "02-why-choose.html": render_why(slug, product),
            "03-formula-quality.html": render_quality(slug, product),
            "04-how-to-use.html": render_usage(slug, product),
        }
        for name, content in files.items():
            (target / name).write_text(content.strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()

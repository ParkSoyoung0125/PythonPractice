from xml.etree.ElementTree import Element, ElementTree, SubElement

mydict = {'hong': ('홍길동', 60, 80, 70), 'park': ('박영희', 50, 70, 95)}

xmlFile = 'XmlTest02.xml'
xmldata = Element('students')

for key, value in mydict.items():
    st = SubElement(xmldata,'student')
    st.attrib['id'] = key

    kor = value[1]
    eng = value[2]
    math = value[3]

    total = kor + eng + math
    avg = total / 3.0

    st.attrib['총점'] = str(total)
    st.attrib['평균'] = '%.2f' % avg

    SubElement(st,'kor').text = str(kor)
    SubElement(st,'eng').text = str(eng)
    SubElement(st,'math').text = str(math)


def indent(elem, level=0):
    mytab = '\t'
    i = '\n' + level * mytab

    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + mytab

        if not elem.tail or not elem.tail.strip():
            elem.tail = i

        for elem in elem:
            indent(elem, level + 1)

        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


# end def

indent(xmldata)

ElementTree(xmldata).write(xmlFile, encoding='utf-8')

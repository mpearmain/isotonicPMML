from datetime import datetime
from xml.etree import ElementTree as ET
from io import BytesIO
from xml.dom import minidom


def topmml(isotonic, datafield_name, targetfield_name, outputfile):
    # Header
    root = ET.Element('PMML', {'xmlns':'http://www.dmg.org/PMML-4_2','version':'4.2'})
    header = ET.SubElement(root,'Header')
    ET.SubElement(header,'Application', {'name' : 'isotonic2pmml', 'version' : '1.0'})
    timestamp = ET.SubElement(header,'Timestamp')
    timestamp.text = datetime.utcnow().isoformat()

    # Data dictionary
    datadictionary = ET.SubElement(root, 'DataDictionary')
    ET.SubElement(datadictionary, 'DataField',
                  {'name' : datafield_name, 'optype' : 'continuous', 'dataType' : 'double'})
    ET.SubElement(datadictionary, 'DataField',
                  {'name' : targetfield_name, 'optype' : 'continuous', 'dataType' : 'double'})

    # Regression model
    regressionmodel = ET.SubElement(root,'RegressionModel',
                                    { 'modelName' : 'Isotonic regression', 'functionName' : 'regression',
                                      'algorithmName' : 'linearRegression'})
    miningschema = ET.SubElement(regressionmodel, 'MiningSchema')
    ET.SubElement(miningschema, 'MiningField', { 'name' : datafield_name })
    ET.SubElement(miningschema, 'MiningField', { 'name' : targetfield_name, 'usageType' : 'target' })
    # Isotonic transformation
    transformationdictionary = ET.SubElement(regressionmodel, 'LocalTransformations')
    derivedfield = ET.SubElement(transformationdictionary, 'DerivedField',
                                 { 'dataType' : 'double', 'name' : 'isotonic', 'optype' :'continuous'})
    normcontinuous = ET.SubElement(derivedfield, 'NormContinuous', { 'field' : datafield_name})
    idx = 0
    for x in isotonic.X_:
        ET.SubElement(normcontinuous, 'LinearNorm',
                      { 'orig' : '%.8f' % x, 'norm' : '%.8f' % isotonic.y_[idx]})
        idx = idx + 1
    # 'Equal' regression table
    regressiontable = ET.SubElement(regressionmodel, 'RegressionTable', {'intercept' : '0.0'})
    ET.SubElement(regressiontable, 'NumericPredictor',
                  {'name' : 'isotonic', 'exponent' : '1', 'coefficient' : '1.0' } )

    # Pretty printing
    tree = ET.ElementTree(root)
    memfile = BytesIO()
    tree.write(memfile, xml_declaration=True, encoding='UTF-8')
    minidom_xml = minidom.parseString(memfile.getvalue().decode('utf-8'))
    pretty_xml = minidom_xml.toprettyxml(encoding='UTF-8')

    # Final output
    file = open(outputfile, 'wb')
    file.write(pretty_xml)

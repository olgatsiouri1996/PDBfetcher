# python3
from gooey import *
import os
# input parameters
@Gooey(required_cols=0, program_name='PDBfetcher', header_bg_color= '#DCDCDC', terminal_font_color= '#DCDCDC', terminal_panel_color= '#DCDCDC')
def main():
    ap = GooeyParser(description="Fetch pdb or fasta file/s from PDB")
    ap.add_argument("-type", "--output type", required=False, type=str, widget='Dropdown', default='1 pdb file', choices=['1 pdb file','1 fasta file','many pdb files','many fasta files','1 multi-fasta file'], help="output type to choose")
    ap.add_argument("-in", "--input txt", required=False, widget='FileChooser', help="1-column input txt file with PDB ids")
    ap.add_argument("-pdb", "--pdb id", required=False, type=str, help="PDB id to retrieve the sequence or pdb file")
    ap.add_argument("-dir", "--output directory", required=False, type=str,widget='DirChooser', help="output directory to save the pdb or fasta file/s per pdb id")
    ap.add_argument("-mfa", "--multi fasta", required=False,widget='FileSaver', help="output multi-fasta file to save sequences for all input pdb ids")
    args = vars(ap.parse_args())
    # choose output  
    outy = args['output type']
    match outy:
        case '1 pdb file':
            os.chdir(args['output directory'])
            os.system(''.join(['curl.exe -s https://files.rcsb.org/view/',args['pdb id'],'.pdb',' > ',args['pdb id'],'.pdb']))
        case '1 fasta file':
            os.chdir(args['output directory'])
            os.system(''.join(['curl.exe -s https://www.rcsb.org/fasta/entry/',args['pdb id'],'/display',' > ',args['pdb id'],'.fasta']))
        case 'many pdb files':
            ids = (str(line.rstrip()) for line in open(args['input txt']))
            os.chdir(args['output directory'])
            for i in ids:
                os.system(''.join(['curl.exe -s https://files.rcsb.org/view/',i,'.pdb',' > ',i,'.pdb']))
        case 'many fasta files':
            ids = (str(line.rstrip()) for line in open(args['input txt']))
            os.chdir(args['output directory'])
            for i in ids:
                os.system(''.join(['curl.exe -s https://www.rcsb.org/fasta/entry/',i,'/display',' > ',i,'.fasta']))
        case '1 multi-fasta file':
            ids = (str(line.rstrip()) for line in open(args['input txt']))
            for i in ids:
                os.system(''.join(['curl.exe -s https://www.rcsb.org/fasta/entry/',i,'/display',' >> ',args['multi fasta']]))        

if __name__ == '__main__':
    main()

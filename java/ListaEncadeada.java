class Node {
    String valor;
    Node proximo;

    Node(String valor) {
        this.valor = valor;
        this.proximo = null;
    }
}

public class ListaEncadeada {

    private Node head;

    public ListaEncadeada() {
        this.head = null;
    }

    public void adicionar(String valor) {
        Node novo = new Node(valor);
        if (head == null) {
            head = novo;
        } else {
            Node atual = head;
            while (atual.proximo != null) {
                atual = atual.proximo;
            }
            atual.proximo = novo;
        }
    }

    public void imprimir() {
        Node atual = head;
        while (atual != null) {
            System.out.print(atual.valor + " ");
            atual = atual.proximo;
        }
        System.out.println();
    }

    public boolean remover(String valor) {
        if (head == null)
            return false;
        if (head.valor.equals(valor)) {
            head = head.proximo;
            return true;
        }
        Node atual = head;
        while (atual.proximo != null) {
            if (atual.proximo.valor.equals(valor)) {
                atual.proximo = atual.proximo.proximo;
                return true;
            }
            atual = atual.proximo;
        }
        return false;
    }

    public int contarOcorrencias(String valor) {
        int count = 0;
        Node atual = head;
        while (atual != null) {
            if (atual.valor.equals(valor)) {
                count++;
            }
            atual = atual.proximo;
        }
        return count;
    }

    public static void main(String[] args) {
        ListaEncadeada lista = new ListaEncadeada();
        lista.adicionar("A");
        lista.adicionar("B");
        lista.adicionar("C");
        lista.imprimir();
        lista.remover("B");
        lista.adicionar("A"); 
        lista.imprimir();
        System.out.println("Ocorrências de 'A': " + lista.contarOcorrencias("A")); 
    }
}
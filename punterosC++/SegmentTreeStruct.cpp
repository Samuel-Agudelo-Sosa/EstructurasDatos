#include<vector>

using namespace std;    

struct Node {
    int l, r, md;
    Node* left = nullptr;
    Node* right = nullptr;
    long long val;

 

    Node(vector<long long>& v, int le, int ri) {
        l = le;
        r = ri;
        md = l + (r - l ) / 2;
        if (l == r){ 
            val = v[l];
            return;
        }
        left = new Node(v, l, md);
        right = new Node(v, md + 1, r);
        val = left->val + right->val;
    }

    void update(int idx, long long value){
        if (l == r) {
            val = value;
            return;
        }
        if(idx <= md){
            left->update(idx, value);
        }
        else{
            right->update(idx,value);
        }
        val = left->val + right->val;
    }

    long long query(int ql, int qr){
        if (r < ql || l > qr)    return 0;
        
        else if (ql <= l && qr >= r) return val;
        
        return left->query(ql, qr) + right->query(ql, qr);
        
    }


    ~Node() {
        delete left;
        delete right;
    }
    
};

